from ..models import Todo, User

def test_todo_model():
    todo = Todo(title="morning workout", description="This included aerobic and strengthening exercises", status_completed="true", user_id="1")
    assert todo.title == "morning workout"
    assert todo.description == "This included aerobic and strengthening exercises"
    assert todo.status_completed == "true"
    assert todo.user_id == "1"

def test_todo_model():
    todo = User(name="Jake", email="Justusjake3@gmail.com",hashed_password="Justusjake3", is_active="True")
    assert todo.name == "Jake"
    assert todo.email == "Justusjake3@gmail.com"
    assert todo.hashed_password == "Justusjake3"
    assert todo.is_active == "True"