import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import env.secrets
import sqlalchemy
from sqlalchemy import Column,Integer,String,Float,DateTime,and_,JSON,Sequence,BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
import time,string,random
import datetime
import json,os

###################### db tables #######
Base=declarative_base()  #  this is metadata for the sqlalchemy table
engine=sqlalchemy.create_engine(os.environ["dburl"])
Session=scoped_session(sessionmaker(bind=engine)) 

#######################################


class Tickers(Base):
    __tablename__="tickers"
    symbol= Column(String(5), primary_key=True)
    name=Column(String(100))
    currency=Column(String(5))
    exchange=Column(String(20),primary_key=True)
    country=Column(String(20))
    type=Column(String(20))


def get_session():
    session=Session()
    session.expire_on_commit=False
    return session

if __name__=="__main__":
    Base.metadata.create_all(engine)



