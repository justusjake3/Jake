from todo.db.models import Todo, User

def test_todo_model(db):
    todo = Todo(title="morning workout", description="This included aerobic and strengthening exercises", status_completed="true", user_id=1)
    assert todo.title == "morning workout"
    assert todo.description == "This included aerobic and strengthening exercises"
    assert todo.status_completed == "true"
    assert todo.user_id == 1

def test_users_model(db):
    users = User(name="Jake", email="Justusjake3@gmail.com", hashed_password="Justusjake", is_active="true")
    assert users.name == "Jake"
    assert users.email == "Justusjake3@gmail.com"
    assert users.hashed_password == "Justusjake"
    assert users.is_active == "true"