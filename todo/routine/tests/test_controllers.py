from ..controllers import TodoController
from ellar.testing import Test, TestClient
from ellar.di import ProviderConfig
from ..services import TodoServices


class TestTodoController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[TodoController], providers=[ProviderConfig(TodoServices, use_class=TodoServices)])
        self.client: TestClient = self.test_module.get_test_client()

    def test_create(self, db, user):
        detail = {
            "title": "morning workout",
            "description": "This included aerobic and strengthening exercises",
            "status_completed": False,
            "user_id": user.id
        }
        response = self.client.post("/routine/create", json=detail)
        assert response.status_code == 201
        data = response.json()
        assert data
        assert data["title"] == detail["title"]
        assert data["description"] == detail["description"]
        assert data["status_completed"] == detail["status_completed"]

    def test_user_routines(self, db, todo):
        response = self.client.get(f"/routine/all/{todo.user_id}")
        data = response.json()
        assert response.status_code == 200
        assert data == [
            {
                'id': 1,
                'title': 'Test routine',
                'description': 'A routine',
                'status_completed': True,
                'user_id': 1,
            }
        ]

    def test_get_list_status_false(self, db, todo):
        response = self.client.get(f"/routine/status/{todo.user_id}?status_completed=false")
        assert response.status_code == 200
        data = response.json()
        assert data == []

    def test_update_routine(self, db, todo):
        updated_data = {
            'id': 1,
            'title': 'Routine update',
            'description': 'An updated routine',
            'status_completed': True,
            "user_id": 1,
        }
        response = self.client.put(f"/routine/{todo.user_id}/{todo.id}", json=updated_data)
        assert response.status_code == 200
        updated_routine = response.json()
        assert updated_routine['title'] == updated_data['title']
        assert updated_routine['description'] == updated_data['description']
        assert updated_routine['user_id'] == updated_data['user_id']
        assert updated_routine['status_completed'] == updated_data['status_completed']
        assert updated_routine['id'] == updated_data['id']

    def test_delete_routine(self, db, todo):
        response = self.client.delete(f"/routine/{todo.user_id}/{todo.id}")
        assert response.status_code == 204
        data = response.json()
        assert data == {}