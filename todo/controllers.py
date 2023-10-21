"""
Define endpoints routes in python class-based fashion
example:

@Controller("/dogs", tag="Dogs", description="Dogs Resources")
class MyController(ControllerBase):
    @get('/')
    def index(self):
        return {'detail': "Welcome Dog's Resources"}
"""
import typing as t
from ellar.common import Controller, ControllerBase, get, put, delete, post
from ellar.common.exceptions import NotFound
from .schemas import TodoSerializer
from .services import TodoServices
from ..todo.database import engine
from ..todo.models import Base
Base.metadata.create_all(bind=engine)


@Controller
class TodoController(ControllerBase):
    def __init__(self, todo_service: TodoServices) -> None:
        self.todo_service = todo_service

    @post("/create", response={201: TodoSerializer})
    async def create_todo(self, todo_data: TodoSerializer):
        todo = self.todo_service.add_todo(todo_data)
        return todo

    @put("/{user_id: str}", response={200: TodoSerializer})
    async def update(self, user_id: str, todo_id: str, payload: TodoSerializer):
        todo = self.todo_service.update(todo_id, user_id, payload.dict())
        if not todo:
            raise NotFound("user not found")
        return todo

    @get("/status", response={200: t.List[TodoSerializer]})
    async def list_status(self, user_id: int, status_completed: bool):
        return self.todo_service.list_completed(user_id, status_completed)

    @delete("/user_todo_id", response={204: dict})
    async def delete(self, user_id: str, todo_id: str):
        todo = self.todo_service.remove(user_id, todo_id)
        if not todo:
            raise NotFound("User's todo not found")
        return 204, {}

    @get("/all", response={200: t.List[TodoSerializer]})
    async def list(self, user_id: int):
        return self.todo_service.list(user_id)



