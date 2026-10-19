
from app.database import initialize_database
from app.services import create_task, get_task, list_tasks
from app.validators import TaskInput


def test_create_and_get_task():
    initialize_database()

    task = create_task(
        TaskInput(title="Service test task", completed=False)
    )

    saved_task = get_task(task["id"])

    assert saved_task is not None
    assert saved_task["title"] == "Service test task"
    assert saved_task["completed"] is False


def test_list_tasks():
    initialize_database()

    task = create_task(
        TaskInput(title="List test task", completed=True)
    )

    tasks = list_tasks()

    assert any(item["id"] == task["id"] for item in tasks)


def test_get_missing_task():
    initialize_database()

    assert get_task(-1) is None
