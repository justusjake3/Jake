from ..controllers import TodoController
from ellar.testing import Test
from ..models import Todo


class TestTodoController:

    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[TodoController])
        self.client = self.test_module.get_test_client()

    def test_create_todo(self):
        detail = {
            "title": "morning workout",
            "description": "This included aerobic and strengthening exercises",
            "status": "Done",
        }
        response = self.client.post("/todo/create", json=detail)
        assert response.status_code == 201
        data = response.json()
        assert data == detail

    def test_list(self):
        response = self.client.get("/todo/")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_get_todo(self):
        response = self.client.get("/todo/")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_update(self):
        detail = {
            "title": "evening workout",
            "description": "This will also include aerobic and strengthening exercises",
            "status": "Undone",
        }
        response = self.client.put("/todo/6", json=detail)
        assert response.status_code == 200
        todo = Todo.query.get(id=8)
        assert todo.title == detail["title"]
        assert todo.description == detail["description"]
        assert todo.status == detail["status"]

    def test_delete(self):
        response = self.client.delete("/todo/6")
        assert response.status_code == 204
        data = response.json()
        assert data
