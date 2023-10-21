"""
Create a provider and declare its scope

@injectable
class AProvider
    pass

@injectable(scope=transient_scope)
class BProvider
    pass
"""
from ellar.di import injectable, singleton_scope
from .models import Todo, User
from ..todo.database import SessionLocal


@injectable(scope=singleton_scope)
class TodoServices:
    def __init__(self) -> None:
        self.database = SessionLocal()

    def add_todo(self, todo_data):
        new_todo = Todo(title=todo_data.title,
                        description=todo_data.description,
                        user_id=todo_data.user_id,
                        status_completed=todo_data.status_completed
                        )
        self.database.add(new_todo)
        self.database.commit()
        self.database.refresh(new_todo)
        return new_todo

    def list(self, user_id):
        todo = self.database.query(Todo).filter(Todo.user_id == user_id).all()
        return todo

    def list_completed(self,user_id,status_completed):
        todo = self.database.query(Todo).filter(Todo.user_id == user_id, Todo.status_completed == status_completed).all()
        return todo

    def update(self,user_id,todo_id,update_data):
        todo = self.database.query(Todo).filter(Todo.user_id == user_id, Todo.id == todo_id)
        todo.update(update_data)
        self.database.commit()
        return todo.first()

    def remove(self, user_id, todo_id):
        delete = self.database.query(Todo).filter(Todo.user_id == user_id, Todo.id == todo_id).delete()
        self.database.commit()
        return delete


