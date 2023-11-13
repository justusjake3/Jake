from ellar.di import ProviderConfig
from todo.user.controllers import UserController
from ..services import UserServices
from ellar.testing import Test, TestClient

class TestUserController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[UserController], providers=[ProviderConfig(UserServices)])
        self.client: TestClient = self.test_module.get_test_client()

    def test_create_user(self, db):
        data = {
            "email": "Justusjake3@gmail.com",
            "name": "Justusjake",
            "hashed_password": "Justusjake",
            "is_active": True,
        }
        response = self.client.post("/user/add", json=data)
        assert response.status_code == 201
        detail = response.json()
        assert detail["id"]
        assert detail["created_date"]
        assert detail["hashed_password"]
        assert detail["email"] == data["email"]
        assert detail["name"] == data["name"]

    def test_get_users(self, user):
        response = self.client.get("/user/")
        assert response.status_code == 200
        data = response.json()
        print(data)
        assert data == [{
            "id": user.id,
            "email": user.email,
            "created_date": user.created_date.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "hashed_password": user.hashed_password,
            "is_active": user.is_active,
            "name": user.name,
        }]

    def test_get_user_by_id(self, user, db):
        response = self.client.get(f"/user/{user.id}")
        assert response.status_code == 200
        data = response.json()
        assert data == {
            "id": user.id,
            "email": user.email,
            "created_date": user.created_date.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "hashed_password": user.hashed_password,
            "is_active": user.is_active,
            "name": user.name,
        }
