from ..controllers import TodoController
from ellar.testing import Test, TestClient
from ellar.di import ProviderConfig
from ..services import TodoServices


class TestTodoController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[TodoController], providers=[ProviderConfig(TodoServices, use_class=TodoServices)])
        self.client: TestClient = self.test_module.get_test_client()

    def test_create(self, db):
        detail = {
            "title": "morning workout",
            "description": "This included aerobic and strengthening exercises",
            "status_completed": False,
            "user_id": 1
        }
        response = self.client.post("/routine/create", json=detail)
        assert response.status_code == 200
        data = response.json()
        assert data
        assert data["title"] == detail["title"]
        assert data["description"] == detail["description"]
        assert data["status_completed"] == detail["status_completed"]

    def test_get_list(self, db):
        user_id = 1
        response = self.client.get(f"/routine/all/{user_id}")
        data = response.json()
        assert response.status_code == 200
        assert data
        print(data)

    def test_get_list_status(self, db):
        response = self.client.get("/routine/status/1?status_completed=false")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_update(self, db):
        detail_update = {
            "title": "evening workout",
            "description": "This will also include aerobic and strengthening exercises",
            #"status": "Undone",
        }
        response = self.client.patch("/routine/1?user_id=1", json=detail_update)
        assert response.status_code == 200
        data = response.json()
        print("for update", data)
        assert data

    def test_delete(self, db):
        response = self.client.delete("/routine/1?user_id=1")
        assert response.status_code == 204
