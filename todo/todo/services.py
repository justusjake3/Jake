from typing import List, Union
from ellar.di import injectable, singleton_scope
from .models import Todo
from ..todo.database import SessionLocal


@injectable(scope=singleton_scope)
class TodoServices:
    def __init__(self) -> None:
        self.database = SessionLocal()

    def add_todo(self, todo_data: dict) -> Todo:
        new_todo = Todo(
            title=todo_data.title,
            description=todo_data.description,
            user_id=todo_data.user_id,
            status_completed=todo_data.status_completed
        )
        self.database.add(new_todo)
        self.database.commit()
        self.database.refresh(new_todo)
        return new_todo

    def list(self, user_id: int) -> List[Todo]:
        todo = self.database.query(Todo).filter(Todo.user_id == user_id).all()
        return todo

    def list_completed(self, user_id: int, status_completed: bool) -> List[Todo]:
        todo = self.database.query(Todo).filter(Todo.user_id == user_id, Todo.status_completed == status_completed).all()
        return todo

    def update(self,user_id: int, todo_id: int, update_data: dict) -> Union[Todo, None]:
        todo = self.database.query(Todo).filter(Todo.user_id == user_id, Todo.id == todo_id)
        todo.update(update_data)
        self.database.commit()
        return todo.first()

    def remove(self, user_id: int, todo_id: int) -> int:
        delete = self.database.query(Todo).filter(Todo.user_id == user_id, Todo.id == todo_id).delete()
        self.database.commit()
        return delete


