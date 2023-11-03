import os
from functools import cache

from ellar.common.constants import ELLAR_CONFIG_MODULE
from ellar.core import Config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/todo"

@cache
def get_engine():
    config = Config(config_module=os.environ.get(ELLAR_CONFIG_MODULE))
    engine = create_engine(config.SQLALCHEMY_URL, connect_args={"check_same_thread": False})
    return engine

def get_session_maker():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
    return SessionLocal

Base = declarative_base()