# from todo.db.models import Todo, User
# class TestModels:
#     def test_users_model(self, db):
#         users = User(name="Jake", email="Justusjake3@gmail.com", hashed_password="Justusjake", is_active=True)
#         db.add(users)
#         db.commit()
#         db.refresh(users)
#         assert users.name == "Jake"
#         assert users.email == "Justusjake3@gmail.com"
#         assert users.hashed_password == "Justusjake"
#         assert users.is_active == True
#
#     def test_routine_model(self, db):
#         routine = Todo(title="morning workout", description="This included aerobic and strengthening exercises", status_completed=True, user_id=1)
#         db.add(routine)
#         db.commit()
#         db.refresh(routine)
#         assert routine.title == "morning workout"
#         assert routine.description == "This included aerobic and strengthening exercises"
#         assert routine.status_completed == True
#         assert routine.user_id == 1
