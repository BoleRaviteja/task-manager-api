
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Python",
            "completed": False,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Learn Python"
    assert data["completed"] is False
    assert isinstance(data["id"], int)


def test_get_missing_task():
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task():
    create_response = client.post(
        "/tasks",
        json={"title": "Update me", "completed": False},
    )
    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        params={"completed": True},
    )

    assert response.status_code == 200
    assert response.json()["completed"] is True
