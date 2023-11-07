import os
from functools import cache

from ellar.common.constants import ELLAR_CONFIG_MODULE
from ellar.core import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


@cache
def get_engine():
    config = Config(config_module=os.environ.get(ELLAR_CONFIG_MODULE, "todo.config:DevelopmentConfig"))
    engine = create_engine(config.SQLALCHEMY_URL)
    return engine

def get_session_maker():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
    return SessionLocal()

Base = declarative_base()