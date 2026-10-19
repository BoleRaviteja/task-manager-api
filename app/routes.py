
from fastapi import APIRouter, HTTPException

from app.services import (
    create_task,
    get_task,
    list_tasks,
    update_task,
)
from app.validators import TaskInput

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/tasks", status_code=201)
def create_task_route(task: TaskInput):
    return create_task(task)


@router.get("/tasks")
def list_tasks_route():
    return list_tasks()


@router.get("/tasks/{task_id}")
def get_task_route(task_id: int):
    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task


@router.patch("/tasks/{task_id}")
def update_task_route(task_id: int, completed: bool):
    task = update_task(task_id, completed)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task
