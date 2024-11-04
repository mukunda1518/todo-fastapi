import uuid
import datetime
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from starlette import status, responses
from starlette.requests import Request
from sqlalchemy.orm import Session

from app.schemas import GetTask, CreateTask, ListTasks
from app.database import get_mysql_db
from app.models import Task, User
from app.auth import validate_token

router = APIRouter()

@router.get("/todo", response_model=ListTasks)
async def get_tasks(request: Request, user=Depends(validate_token), db: Session = Depends(get_mysql_db)):
    user_id = user.get("sub")
    tasks = [
        task.dict() for task in db.query(User).filter(User.id == user_id).first().tasks
    ]
    return {"tasks": tasks}

@router.post("/todo", response_model=GetTask, status_code=status.HTTP_201_CREATED)
async def create_task(request: Request, payload: CreateTask, user=Depends(validate_token), db: Session = Depends(get_mysql_db)):
    task = Task(
        created=datetime.datetime.now(),
        updated=datetime.datetime.now(),
        title=payload.title,
        description=payload.description,
        priority=payload.priority.value,
        status=payload.status.value,
        user_id=request.state.user_id
    )
    db.add(task)
    db.commit()
    task = task.dict()
    return task

@router.get("/todo/{task_id}", response_model=GetTask)
async def get_task(request: Request, task_id: uuid.UUID, user=Depends(validate_token), db: Session = Depends(get_mysql_db)):
    task = db.query(Task).filter(
        Task.id == str(task_id), Task.user_id == request.state.user_id
    ).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task.dict()

@router.put("/todo/{task_id}", response_model=GetTask)
async def update_task(request: Request, task_id: uuid.UUID, payload: CreateTask, user=Depends(validate_token), db: Session = Depends(get_mysql_db)):
    task = db.query(Task).filter(
        Task.id == str(task_id), Task.user_id == request.state.user_id
    ).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = payload.title
    task.description = payload.description
    task.priority = payload.priority.value
    task.status = payload.status.value
    task.updated = datetime.datetime.now()
    db.add(task)
    db.commit()
    task = task.dict()
    return task

@router.delete("/todo/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(request: Request, task_id: uuid.UUID,  user=Depends(validate_token), db: Session = Depends(get_mysql_db)):
    task = db.query(Task).filter(
        Task.id == str(task_id), Task.user_id == request.state.user_id
    ).first()
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    db.delete(task)
    db.commit()

