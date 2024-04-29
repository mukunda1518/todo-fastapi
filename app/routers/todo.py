import uuid
import datetime
from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status, responses
from starlette.requests import Request

from app.schemas import GetTask, CreateTask, ListTasks

router = APIRouter()

TODO = []

@router.get("/todo", response_model=ListTasks)
def get_tasks(request: Request):
    import ipdb ; ipdb.set_trace()
    user_id = request.state.user_id
    return {
        "tasks": TODO
    }

@router.post("/todo", response_model=GetTask, status_code=status.HTTP_201_CREATED)
def create_task(payload: CreateTask):
    task = {}
    task['id'] = uuid.uuid4()
    task["created"] = datetime.datetime.now()
    task["title"] = payload.title
    task["description"] = payload.description
    task["priority"] = payload.priority
    task["status"] = payload.status
    TODO.append(task)
    return task

@router.get("/todo/{task_id}", response_model=GetTask)
def get_task(task_id: uuid.UUID):
    for task in TODO:
        if task_id == task["id"]:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/todo/{task_id}", response_model=GetTask)
def update_task(task_id: uuid.UUID, payload: CreateTask):
    for task in TODO:
        if task_id == task["id"]:
            task["title"] = payload.title
            task["description"] = payload.description
            task["priority"] = payload.priority
            task["status"] = payload.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/todo/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: uuid.UUID):
    for index, task in enumerate(TODO):
        if task['id'] == task_id:
            TODO.pop(index)
            return
    raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
