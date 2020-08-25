import numpy as np
import io
from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from . import models
from . import opdb


def fetch_proposal(url):
    db = opdb.OpDB()
    db.dbinfo = url
    db.connect()
    df = db.fetch_all('proposal')
    db.close()
    return df


def insert_proposal(url, dataframe):
    db = opdb.OpDB()
    db.dbinfo = url
    db.connect()
    db.insert('proposal', dataframe)
    db.close()
    return 0
