import typing as t
from ellar.common import Controller, ControllerBase, get, post
from ellar.common.exceptions import NotFound
from .schemas import UserSerializer
from .services import UserServices


@Controller("/user")
class UserController(ControllerBase):
    def __init__(self, user_service: UserServices) -> None:
        self.user_service = user_service

    @post("/add", response={201: UserSerializer})
    async def create_user(self, user_data: UserSerializer) -> t.Dict:
        user = self.user_service.create_user(user_data)
        return user

    @get("/", response={200: t.List[UserSerializer]})
    async def list_users(self) -> t.List[t.Dict]:
        return self.user_service.get_all_users()

    @get("/{user_id}", response={200: UserSerializer})
    async def get_user_by_id(self, user_id: int) -> t.Optional[dict]:
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise NotFound("User's routine not found")
        return user



