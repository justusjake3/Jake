from ..controllers import TodoController
from ellar.testing import Test, TestClient
from ellar.di import ProviderConfig
from ..services import TodoServices


class TestTodoController:

    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[TodoController], providers=[ProviderConfig(TodoServices, use_class=TodoServices)])
        self.client: TestClient = self.test_module.get_test_client()
        self.detail = {
            "title": "morning workout",
            "description": "This included aerobic and strengthening exercises",
            "status_completed": False,
        }

    def test_create_todo(self, db, user_create):
        self.detail.update({"user_id": user_create.id})
        response = self.client.post("/todo/create", json=self.detail)
        assert response.status_code == 200
        data = response.json()
        assert data
        assert data["title"] == self.detail["title"]
        assert data["description"] == self.detail["description"]
        assert data["status_completed"] == self.detail["status_completed"]

    def test_get_list(self, db):
        user_id = 1
        response = self.client.get(f"/todo/all/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data
        print(data)

    def test_get_list_status(self, db):
        response = self.client.get("/todo/status/1?status_completed=false")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_update(self, db, user_create):
        detail_update = {
            "title": "evening workout",
            "description": "This will also include aerobic and strengthening exercises",
            "status": "Undone",
        }
        response = self.client.put("/todo/1?todo_id=1", json=detail_update)
        assert response.status_code == 200
        data = response.json()
        print(data)
        assert data

    def test_delete(self, db):
        response = self.client.delete("/todo/1?todo_id=1")
        assert response.status_code == 204
