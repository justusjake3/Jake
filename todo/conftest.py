import asyncio
import os
from pathlib import Path

import alembic.config
from alembic.config import Config
from alembic.command import upgrade, downgrade
import pytest
from ellar.common.constants import ELLAR_CONFIG_MODULE
from ellar.core import App
from ellar.testing import Test
from ellar.testing.module import TestingModule
from httpx import AsyncClient
from sqlalchemy import text, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine

from .todo.models import Base, User
from .todo.database import get_session_maker
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

# @pytest.fixture(scope="session")
# async def _db_engine(app):
#     engine = app.injector.get(AsyncEngine)
#
#     async with engine.connect() as conn:
#         await conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
#         await conn.commit()
#
#     try:
#         async with engine.begin() as conn:
#             await conn.run_sync(Base.metadata.drop_all)
#     finally:
#         try:
#             yield
#         except Exception:
#             pass
#
#         async with engine.connect() as conn:
#             await conn.execute(text("DROP TABLE alembic_version"))
#             await conn.commit()
#
#         async with engine.begin() as conn:
#             await conn.run_sync(Base.metadata.drop_all)
#
#         await engine.dispose()

@pytest.fixture(scope="session")
def migration_config() -> Config:
    config = Config()


    config.set_main_option(name: 'script_location', os.path.join(str(Path(__file__).parent), 'migration'))


    return config


@pytest.fixture(scope="session")
def db(app, migration_config ):
    engine = create_engine(app.config.SQLALCHEMY_URL, connect_args={"check_same_thread": False})

    try:
        Base.metadata.drop_all(bind=engine)
        upgrade(migration_config, revision='head')

        yield
    except Exception:
        pass

        Base.metadata.drop_all(bind=engine)
        downgrade(migration_config, revision='')
        engine.dispose()

@pytest.fixture()
def user_create(app):
    session = get_session_maker(app.config)()
    user_details = {
        "email": "Justusjake3@gmail.com",
        "name": "Justusjake",
        "hashed_password": "Justusjake",
        "is_active": True
    }
    user = User(**user_details)
    session.add(user)
    session.commit()
    session.refresh(user)

    yield user
    session.query(User).filter(User.id == user.id).delete()
    session.commit()