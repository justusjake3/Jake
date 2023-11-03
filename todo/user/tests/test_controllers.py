from ellar.di import ProviderConfig

from todo.user.controllers import UserController
from ..services import UserServices
from ellar.testing import Test, TestClient



class TestUserController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[UserController], providers=[ProviderConfig(UserServices)])
        self.client: TestClient = self.test_module.get_test_client()

    def test_user_create(self, db):
        data = {
            "email": "Justusjake3@gmail.com",
            "name": "Justusjake",
            "hashed_password": "Justusjake",
            "is_active": True,
        }
        response = self.client.post("/user/add", json=data)
        assert response.status_code == 200
        detail = response.json()
        assert detail["id"]
        assert detail["created_date"]
        assert detail["hashed_password"]
        assert detail["email"] == data["email"]
        assert detail["name"] == data["name"]

    def test_user_get(self, db):
        response = self.client.get("/user/")
        assert response.status_code == 200
        data = response.json()
        print(data)
        assert data

    def test_get_user_id(self, db):
        user_id = 1
        response = self.client.get(f"/user/{user_id}")
        assert response.status_code == 200
        user = response.json()
        assert user
        print(user)