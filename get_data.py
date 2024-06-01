from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Task
from datetime import datetime

session_maker = sessionmaker(bind=create_engine("mysql://todo_user:todo_pass@localhost:3306/todo_db"))

with session_maker() as session:
    users = session.query(User).all()
    for user in users:
        print(user.dict())
        
