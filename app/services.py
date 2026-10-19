
from app.database import get_connection
from app.validators import TaskInput


def create_task(task: TaskInput) -> dict:
    with get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, ?)",
            (task.title, int(task.completed)),
        )
        task_id = cursor.lastrowid

        row = connection.execute(
            "SELECT id, title, completed FROM tasks WHERE id = ?",
            (task_id,),
        ).fetchone()

        return {
            "id": row["id"],
            "title": row["title"],
            "completed": bool(row["completed"]),
        }


def list_tasks() -> list[dict]:
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, title, completed FROM tasks ORDER BY id"
        ).fetchall()

        return [
            {
                "id": row["id"],
                "title": row["title"],
                "completed": bool(row["completed"]),
            }
            for row in rows
        ]


def get_task(task_id: int) -> dict | None:
    with get_connection() as connection:
        row = connection.execute(
            "SELECT id, title, completed FROM tasks WHERE id = ?",
            (task_id,),
        ).fetchone()

        if row is None:
            return None

        return {
            "id": row["id"],
            "title": row["title"],
            "completed": bool(row["completed"]),
        }


def update_task(task_id: int, completed: bool) -> dict | None:
    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE tasks SET completed = ? WHERE id = ?",
            (int(completed), task_id),
        )

        if cursor.rowcount == 0:
            return None

        row = connection.execute(
            "SELECT id, title, completed FROM tasks WHERE id = ?",
            (task_id,),
        ).fetchone()

        return {
            "id": row["id"],
            "title": row["title"],
            "completed": bool(row["completed"]),
        }
