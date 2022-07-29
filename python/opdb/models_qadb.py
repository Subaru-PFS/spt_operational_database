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


class e2e_processing(Base):
    __tablename__ = 'e2e_processing'

    run_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    run_description = Column(String,
                             comment='description of the processing run')
    run_status = Column(String,
                        comment='status of the processing run')
    run_datetime_start = Column(DateTime,
                                comment='datetime of the processing run start')
    run_datetime_end = Column(DateTime,
                              comment='datetime of the processing run end')

    def __init__(self,
                 run_description,
                 run_datetime_start,
                 run_datetime_end,
                 ):
        self.run_description = run_description
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
