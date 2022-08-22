from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Integer, String, FLOAT, ForeignKey, DateTime, Boolean, REAL, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation, backref
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql.schema import PrimaryKeyConstraint

Base = declarative_base()


class test(Base):
    __tablename__ = 'test'

    test_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    test_val1 = Column(Integer, comment='test_val1')
    test_val2 = Column(REAL, comment='test_val2')
    test_val3 = Column(String, comment='test_val3')
    test_val4 = Column(DateTime, comment='test_val4')

    def __init__(self, test_val1, test_val2, test_val3, test_val4):
        self.test_val1 = test_val1
        self.test_val2 = test_val2
        self.test_val3 = test_val3
        self.test_val4 = test_val4


class e2e_sim_dataset(Base):
    __tablename__ = 'e2e_sim_dataset'

    dataset_id = Column(Integer,
                        primary_key=True,
                        unique=True,
                        autoincrement=True,
                        comment='sim dataset id'
                        )
    dataset_description = Column(String,
                                 comment='sim dataset description'
                                 )
    sim2d_version = Column(String,
                           comment='simulator version for the dataset'
                           )
    created_at = Column(DateTime,
                        comment='datetime that the dataset was made'
                        )

    def __init__(self,
                 dataset_id,
                 dataset_description,
                 sim2d_version,
                 created_at
                 ):
        self.dataset_id = run_descrdataset_idiption
        self.dataset_description = dataset_description
        self.sim2d_version = sim2d_version
        self.created_at = created_at


class e2e_processing(Base):
    __tablename__ = 'e2e_processing'

    run_id = Column(Integer,
                    primary_key=True,
                    unique=True,
                    autoincrement=True)
    run_description = Column(String,
                             comment='description of the processing run')
    run_sample = Column(String,
                        comment='sample of the processing run (weekly/extended)')
    run_dataset = Column(Integer,
                         ForeignKey('e2e_sim_dataset.dataset_id'),
                         comment='sim dataset id'
                         )
    run_status = Column(String,
                        comment='status of the processing run')
    run_datetime_start = Column(DateTime,
                                comment='datetime of the processing run start')
    run_datetime_end = Column(DateTime,
                              comment='datetime of the processing run end')

    def __init__(self,
                 run_description,
                 run_sample,
                 run_datetime_start,
                 run_datetime_end,
                 ):
        self.run_description = run_description
        self.run_sample = run_sample
        self.run_datetime_start = run_datetime_start
        self.run_datetime_end = run_datetime_end


class e2e_drp_version(Base):
    __tablename__ = 'e2e_drp_version'

    run_id = Column(Integer,
                    ForeignKey('e2e_processing.run_id'),
                    primary_key=True,
                    )
    drp2d_version = Column(String,
                           comment='DRP2D version'
                           )
    drp1d_amazed_version = Column(String,
                                  comment='DRP1D (Amazed) version'
                                  )
    drp1d_client_version = Column(String,
                                  comment='DRP1D (PFS client) version'
                                  )

    def __init__(self,
                 run_id,
                 drp2d_version,
                 drp1d_amazed_version,
                 drp1d_client_version,
                 ):
        self.run_id = run_id
        self.drp2d_version = drp2d_version
        self.drp1d_amazed_version = drp1d_amazed_version
        self.drp1d_client_version = drp1d_client_version


class e2e_qa_redshift(Base):
    __tablename__ = 'e2e_qa_redshift'

    run_id = Column(Integer,
                    ForeignKey('e2e_processing.run_id'),
                    primary_key=True,
                    )
    num_targets = Column(Integer,
                         comment='number of targets in this QA')
    diff_mean = Column(REAL,
                       comment='mean offset')
    diff_std = Column(REAL,
                      comment='standard deviation of the difference')
    frac_outlier = Column(REAL,
                          comment='fraction of outliers (abs(diff)>3sigma)')

    e2e_processing = relation(e2e_processing, backref=backref('e2e_qa_redshift'))

    def __init__(self,
                 run_id,
                 num_targets,
                 diff_mean,
                 diff_std,
                 frac_outlier,
                 ):
        self.run_id = run_id
        self.num_targets = num_targets
        self.diff_mean = diff_mean
        self.diff_std = diff_std
        self.frac_outlier = frac_outlier


class reduced_visits(Base):
    __tablename__ = 'reduced_visits'

    pfs_visit_id = Column(Integer,
                          primary_key=True,
                          unique=True,
                          autoincrement=False)
    is_ingested = Column(Boolean, comment='ingested?')
    is_isred = Column(Boolean, comment='ISRed?')
    is_reduced = Column(Boolean, comment='reduceExposure.py done?')
    is_merged = Column(Boolean, comment='pfsArm merged?')
    is_calibrated = Column(Boolean, comment='flux calibrated?')
    is_coadded = Column(Boolean, comment='coadded?')
    updated_at = Column(DateTime,
                        comment='datetime of the table update')

    def __init__(self,
                 pfs_visit_id,
                 is_ingested,
                 is_reduced,
                 is_merged,
                 is_calibrated,
                 is_coadded,
                 updated_at,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.is_isred = is_isred
        self.is_reduced = is_reduced
        self.is_merged = is_merged
        self.is_calibrated = is_calibrated
        self.is_coadded = is_coadded
        self.updated_at = updated_at


class data_processing(Base):
    __tablename__ = 'data_processing'

    run_id = Column(Integer,
                    primary_key=True,
                    unique=True,
                    autoincrement=True)
    pfs_visit_id = Column(Integer,
                          ForeignKey('reduced_visits.pfs_visit_id'),
                          comment='PFS visit identifier')
    run_description = Column(String,
                             comment='description of the processing run')
    run_status = Column(String,
                        comment='status of the processing run')
    run_datetime_start = Column(DateTime,
                                comment='datetime of the processing run start')
    run_datetime_end = Column(DateTime,
                              comment='datetime of the processing run end')

    reduced_visits = relation(reduced_visits, backref=backref('data_processing'))

    def __init__(self,
                 pfs_visit_id,
                 run_description,
                 run_sample,
                 run_datetime_start,
                 run_datetime_end,
                 ):
        self.pfs_visit_id = pfs_visit_id
        self.run_description = run_description
        self.run_sample = run_sample
        self.run_datetime_start = run_datetime_start
        self.run_datetime_end = run_datetime_end


def make_database(dbinfo):
    '''
    dbinfo is something like this: postgresql://xxxxx:yyyyy@zzz.zzz.zzz.zz/dbname
    '''
    # engine = create_engine('sqlite:///:memory:', echo=True)
    # engine = create_engine('sqlite:///pfs_proto.sqlite', echo=False)
    engine = create_engine(dbinfo)

    Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session()


if __name__ == '__main__':
    import sys
    dbinfo = sys.argv[1]
    print(dbinfo)
    make_database(dbinfo)
