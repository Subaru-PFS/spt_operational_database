from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

from . import models


def create_schema(dbinfo, drop_all=False):
    '''
    dbinfo is something like this: dialect://username:passwd@hostname:port/dbname
    '''
    engine = create_engine(dbinfo)
    if drop_all:
        models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)
