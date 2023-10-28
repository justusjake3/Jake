import typing as t
from typing import List
from ellar.common import Controller, ControllerBase, get, post
from ellar.common.exceptions import NotFound
from .schemas import UserSerializer
from .services import UserServices
from ..todo.database import engine
from ..todo.models import Base, User
Base.metadata.create_all(bind=engine)


@Controller("/user")
class UserController(ControllerBase):
    def __init__(self, user_service: UserServices) -> None:
        self.user_service = user_service

    @post("/add", response={201: UserSerializer})
    async def create_user(self, user_data: UserSerializer) -> User:
        user = self.user_service.create_user(user_data)
        return user

    @get("/", response={200: t.List[UserSerializer]})
    async def list_users(self) -> List[UserSerializer]:
        return self.user_service.get_all_users()

    @get("/{user_id: str}", response={200: UserSerializer})
    async def get_user_by_id(self, user_id: int) -> UserSerializer:
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise NotFound("User's todo not found")
        return user



