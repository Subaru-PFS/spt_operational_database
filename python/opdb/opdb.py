import io
import logging

import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from opdb import models


class OpDB(object):
    """
        === CAUTION! ===

        We remove `password` argument at some point.
        Password should be written in .pgpass

        ================
    """

    url = 'postgresql://pfs@db-ics:5432/opdb'

    def __init__(self, hostname='localhost', port='5432', dbname='test', username='test', dialect='postgresql'):
        self.dbinfo = "{0}://{1}@{2}:{3}/{4}".format(dialect,
                                                     username,
                                                     hostname,
                                                     port,
                                                     dbname)
        self.logger = logging.getLogger('opdb')
        self.connect()

    def connect(self):
        self.engine = create_engine(self.dbinfo, poolclass=sqlalchemy.pool.NullPool)
        SessionClass = sessionmaker(self.engine)
        self.session = SessionClass()

    def close(self):
        self.session.close()

    def rollback(self):
        self.session.rollback()

############################################################
# functionality to insert/update information into the database
############################################################

    def insert(self, tablename, dataframe):
        """
        Insert DataFrame rows into a mapped table inside a managed transaction.

        Behavior
        --------
        - Opens `with self.session.begin():` to wrap the bulk insert in a single transaction.
          Commits on success, rolls back on exception.
        - Use this when you want the helper to manage the transaction boundary.

        Requirements
        ------------
        - `tablename` is the name of a mapped model in `models`.
        - `dataframe` columns must match the table columns; values must be coercible to DB types.

        Notes
        -----
        - Uses `bulk_insert_mappings` under the hood for speed (bypasses ORM events/per-row validation).
        """
        with self.session.begin():
            self.bulk_insert_mappings(tablename, dataframe)

    def bulk_insert_mappings(self, tablename, dataframe):
        """
        Bulk-insert DataFrame rows using SQLAlchemy's `bulk_insert_mappings`.

        Behavior
        --------
        - Reuses the current Session transaction; does not call `begin()`/`commit()`.
          The caller controls commit/rollback.
        - Fast path: minimal ORM overhead (no per-row flush events; DB-side defaults not round-tripped).

        Parameters
        ----------
        tablename : str
            Name of the mapped model in `models`.
        dataframe : pandas.DataFrame
            Data to insert; columns must match the table schema.

        Example
        -------
        # Caller-managed transaction (reuse existing txn)
        with self.session.begin():
            self.bulk_insert_mappings('mcs_pfi_transformation', df)
        """
        model = getattr(models, tablename)
        mappings = dataframe.to_dict(orient="records")
        self.session.bulk_insert_mappings(model, mappings)

##################################################
# functionality to get information from the database
##################################################

    def fetch_query(self, query):
        """
            Description
            -----------
                Get all records from SQL query

            Parameters
            ----------
                query : `string`

            Returns
            -------
                df : `pandas.DataFrame`

            Note
            ----
        """
        try:
            df = pd.read_sql(query, self.session.bind)
        except:
            self.session.rollback()
            raise

        return df


    # These are the pg_type oids for all the known and used PFS data
    # types. There are many many more. If we really cared there is
    # probably a complicated way to use the rest of the pg_type table
    # to construct numpy dtypes.
    _pgTypes = {16: np.bool_,
                20: np.int64,
                23: np.int32,
                700: np.float32,
                701: np.float64,
                1043: str,  # varchar, we want variable length string
                1114: np.dtype('datetime64[us]'),  # nb: numpy does not do timezones
                }

    def _getColTypes(self, tablename):
        """Retrieve mapping of numpy dtypes for all the columns in a table"""

        pgdesc = []
        dtypes = {}
        with self.engine.begin() as conn:
            with conn.connection.cursor() as cursor:
                cursor.execute(f'select * from {tablename} where False')
                pgdesc = cursor.description

        for col in pgdesc:
            code = col.type_code
            dtype = self._pgTypes[code]
            dtypes[col.name] = dtype

        return dtypes

    def bulkSelect(self, tablename, selectSql=None):
        """Efficiently retrieve selected records from a table.

        Returns a pandas dataframe of all the columns, trying to get
        the numpy types appropriate for the SQL types.

        The tablename and the selectSql statement can be
        incompatible. We do not check; the only effect would be that
        the numpy dtypes will be whatever pandas intuits.

        The selectSql statement can be *any* single SELECT statement
        which our versinof postgresql accepts in COPY TO statments. If
        no statement is passed the entire table is returned. Caveat
        executor, or something.

        Parameters
        ----------
        tablename : `str`
            The tablename. If not None we fetch the table's column types.
        selectSql : `str`
            The optional sql select statement.

        Returns
        -------
        data      : `pandas.DataFrame`
           Always contains all columns.
        """

        if tablename is not None:
            dtypes = self._getColTypes(tablename)
        else:
            dtypes = None  # Let pandas auto-detect dtypes

        if selectSql is None:
            sql = f'COPY {tablename}'
        else:
            sql = f'COPY ({selectSql})'

        sqlCmd = f"{sql} TO STDOUT WITH (FORMAT csv, HEADER)"
        self.logger.info(f'fetching sql: {sqlCmd}')

        buf = io.StringIO()
        with self.engine.begin() as conn:
            with conn.connection.cursor() as cursor:
                cursor.copy_expert(sqlCmd, buf)
        if buf.tell() == 0:
            self.logger.warn(f'no data read for: {sqlCmd}')
            return None

        buf.seek(0, 0)
        df = pd.read_csv(buf, header=0, dtype=dtypes)
        return df

    def bulkInsert(self, tablename, data):
        """Efficiently insert DataFrame rows into a table.

        UNTESTED as of 2021-07-22

        The data needs to match the structure of the named table well
        enough. We do not check at all.

        Parameters
        ----------
        tablename : `string`
            The tablename to insert into.
        data : `pandas.DataFrame`
            The data to insert.
        """

        buf = io.StringIO()
        data.to_csv(buf, header=False, index=False)
        buf.seek(0)

        sqlCmd = f"COPY {tablename} FROM STDIN WITH (FORMAT csv)"

        with self.engine.begin() as conn:
            with conn.connection.cursor() as cursor:
                try:
                    cursor.copy_expert(sqlCmd, buf)
                except Exception as e:
                    print(e)
