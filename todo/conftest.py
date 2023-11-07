import asyncio
import os

from alembic.command import upgrade
import pytest
from alembic.config import Config
from ellar.common.constants import ELLAR_CONFIG_MODULE
from ellar.core import App
from ellar.testing import Test
from ellar.testing.module import TestingModule
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db.models import Base, User
from .root_module import ApplicationModule

os.environ.setdefault(ELLAR_CONFIG_MODULE, "todo.config:TestConfig")

@pytest.fixture(scope="session")
def test_module() -> TestingModule:
    return Test.create_test_module(modules=[ApplicationModule])


@pytest.fixture(scope="session")
def app(test_module: TestingModule) -> App:
    return test_module.create_application()


@pytest.fixture(scope="session")
def client(app: App) -> AsyncClient:  # type: ignore[misc]
    with AsyncClient(app=app, base_url="http://testserver.com") as ac:
        yield ac


@pytest.fixture(autouse=True, scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()

@pytest.fixture(scope="session")
def migration_config() -> Config:
    config = Config()

    config.set_main_option('script_location', 'db/alembic')

    return config


@pytest.fixture(scope="session")
def db_engine(app, migration_config):
    engine = create_engine(app.config.SQLALCHEMY_URL)
    Base.metadata.create_all(bind=engine)
    upgrade(migration_config, revision='head')

    yield engine

    Base.metadata.drop_all(bind=engine)
    engine.dispose()

@pytest.fixture(scope="session")
def db(app, db_engine):
    session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session.begin()
    yield session()
    session.close_all()


@pytest.fixture(scope="session")
def create_user(db):
    user = User(id=1,
                email="Justusjake3@gmail.com",
                name="Justusjake",
                hashed_password="Justusjake",
                is_active=True
                )
    db.add(user)
    db.commit()
    db.refresh(user)
    yield user
