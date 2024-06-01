import uuid

from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import Base


def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "user"

    id = Column(String(50), primary_key=True, default=generate_uuid)
    created = Column(DateTime, nullable=False)
    email = Column(String(50), nullable=False)

    tasks = relationship("Task")

    def dict(self):
        return {
            "id": self.id,
            "created": self.created,
            "email": self.email,
            "tasks": self.tasks
        }

class Task(Base):
    __tablename__ = "task"

    id = Column(String(50), primary_key=True, default=generate_uuid)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=False)
    title = Column(String(300), nullable=False)
    description = Column(Text, nullable=True)
    priority = Column(String(20), nullable=False)
    status = Column(String(50), nullable=False)
    user_id = Column(String(50), ForeignKey("user.id"), nullable=False)

    def dict(self):
        return {
            "id": self.id,
            "created": self.created,
            "updated": self.updated,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }
