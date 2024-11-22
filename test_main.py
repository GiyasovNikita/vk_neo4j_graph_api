import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Тестовый клиент FastAPI
client = TestClient(app)

# Фиктивный токен для авторизации
TEST_TOKEN = os.getenv("AUTH_TOKEN", "test-token")


@pytest.fixture
def auth_header():
    """Фикстура для передачи токена авторизации."""
    return {"Authorization": f"Bearer {TEST_TOKEN}"}


def test_get_nodes(auth_header):
    """Тест на получение всех узлов."""
    response = client.get("/nodes", headers=auth_header)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_node_and_relationships(auth_header):
    """Тест на получение узла и всех его связей."""
    # Перед тестом убедитесь, что узел с ID 1 существует
    node_id = 1
    response = client.get(f"/node/{node_id}", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert "n" in data[0]  # Проверяем, что узел возвращается
    assert "r" in data[0]  # Проверяем, что связь возвращается
    assert "m" in data[0]  # Проверяем, что конечный узел возвращается


def test_insert_node_and_relationships(auth_header):
    """Тест на добавление узла и связей."""
    test_data = {
        "node": {
            "id": 17763,
            "label": "User",
            "name": "Jane Doe",
            "screen_name": "janedoe",
            "sex": 2,
            "home_town": "San Francisco"
        },
        "relationships": [
            {"id": 19842, "type": "Follow", "end_node_id": 2548}
        ]
    }
    response = client.post("/insert", json=test_data, headers=auth_header)
    assert response.status_code == 200
    assert response.json() == {"status": "Node and relationships added"}


def test_delete_node_and_relationships(auth_header):
    """Тест на удаление узла и его связей."""
    node_id = 17763  # ID узла, добавленного в предыдущем тесте
    response = client.delete(f"/node/{node_id}", headers=auth_header)
    assert response.status_code == 200
    assert response.json() == {"status": f"Node {node_id} and its relationships deleted"}
