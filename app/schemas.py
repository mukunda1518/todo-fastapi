from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class Error(BaseModel):
    detail: str

class Priority(Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Status(Enum):
    todo = "todo"
    progress = "progress"
    pending = "pending"
    completed = "completed"

class CreateTask(BaseModel):
    title: str
    description: Optional[str] = ""
    priority: Optional[Priority] = Priority.low
    status: Optional[Status] = Status.todo


class GetTask(BaseModel):
    id: UUID
    created: datetime
    title: str
    description: Optional[str] = ""
    priority: Optional[Priority] = Priority.low
    status: Optional[Status] = Status.todo

class ListTasks(BaseModel):
    tasks: List[GetTask] = []