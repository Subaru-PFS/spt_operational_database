import pandas as pd
from . import opdb

'''
    ############################################################
    functionality to insert/update information into the database
    ############################################################
'''


def insert_row(url, tablename, **kwargs):
    '''
        Description
        -----------
            Insert information into a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            dataframe : `pandas.DataFrame`

        Returns
        -------
            None

        Note
        ----
            Column labels of `dataframe` should be exactly the same as those of the table
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        db.insert_mappings(tablename, [kwargs])
    finally:
        db.close()
    return 0


def insert(url, tablename, dataframe):
    '''
        Description
        -----------
            Insert information into a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            dataframe : `pandas.DataFrame`

        Returns
        -------
            None

        Note
        ----
            Column labels of `dataframe` should be exactly the same as those of the table
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        db.insert(tablename, dataframe)
    finally:
        db.close()
    return 0


def insert_by_copy(url, tablename, data, colnames):
    '''
        Description
        -----------
            Insert information into a table

        Parameters
        ----------
            url      : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            data     : `io.StringIO` (comma-separated)
            colnames : `list` of `string`

        Returns
        -------
            None

        Note
        ----
            Column labels of `dataframe` should be exactly the same as those of the table
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        db.insert_by_copy(tablename, data, colnames)
    finally:
        db.close()
    return 0


def update(url, tablename, dataframe):
    '''
        Description
        -----------
            Update information of a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            dataframe : `pandas.DataFrame`

        Returns
        -------
            None

        Note
        ----
            Column labels of `dataframe` should be exactly the same as those of the table
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        db.update(tablename, dataframe)
    finally:
        db.close()
    return 0


def insert_pfs_design(url, pfsDesign, tile_id):
    '''
        Description
        -----------
            Extract information from pfsDesign object and insert into `pfs_design` & `pfs_design_fiber`

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            pfsDesign : `pfsDesign` object
            tile_id : `int`

        Returns
        -------
            None

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    ''' insert `pfs_design` '''
    df = pd.DataFrame({'pfs_design_id': [pfsDesign.pfsDesignId],
                       'tile_id': [tile_id],
                       'ra_center_designed': [pfsDesign.raBoresight],
                       'dec_center_designed': [pfsDesign.decBoresight]
                       })
    try:
        db.connect()
        db.insert('pfs_design', df)
    finally:
        db.close()
    ''' insert `pfs_design_fiber` '''
    cobra_id = pfsDesign.fiberId
    df = pd.DataFrame({'pfs_design_id': [pfsDesign.pfsDesignId for _ in cobra_id],
                       'cobra_id': cobra_id,
                       'pfi_nominal_x_mm': pfsDesign.pfiNominal.transpose()[0],
                       'pfi_nominal_y_mm': pfsDesign.pfiNominal.transpose()[1]
                       })
    try:
        db.connect()
        db.insert('pfs_design_fiber', df)
    finally:
        db.close()

    return 0

'''
    ##################################################
    functionality to get information from the database
    ##################################################
'''


def fetch_all(url, tablename):
    '''
        Description
        -----------
            Get all records from a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`

        Returns
        -------
            df : `pandas.DataFrame`

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        df = db.fetch_all(tablename)
    finally:
        db.close()
    return df


def fetch_query(url, query):
    '''
        Description
        -----------
            Get all records from SQL query

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            query : `string`

        Returns
        -------
            df : `pandas.DataFrame`

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        df = db.fetch_query(query)
    finally:
        db.close()
    return df


def fetch_by_id(url, tablename, **kwargs):
    '''
        Description
        -----------
            Get records from a table where the keyword identifier is matched

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            **kwargs  :          (e.g., pfs_visit_id=12345)

        Returns
        -------
            df : `pandas.DataFrame`

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        df = db.fetch_by_id(tablename, **kwargs)
    finally:
        db.close()
    return df


def fetch_by_copy(url, tablename, colnames):
    '''
        Description
        -----------
            Insert information into a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            colnames  : `list` of `string`

        Returns
        -------
            res       : `io.StringIO` (comma-separated)

        Note
        ----
            Column labels of `dataframe` should be exactly the same as those of the table
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    res = None
    try:
        db.connect()
        res = db.fetch_by_copy(tablename, colnames)
    finally:
        db.close()
    return res


def fetch_sps_exposures(url, pfs_visit_id):
    '''
        Description
        -----------
            Get SpS exposure information for a given `pfs_visit_id`

        Parameters
        ----------
            url          : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            pfs_visit_id : `int`

        Returns
        -------
            df : `pandas.DataFrame`

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        df = db.fetch_sps_exposures(pfs_visit_id=pfs_visit_id)
    finally:
        db.close()
    return df
