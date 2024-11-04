from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Task
from datetime import datetime


users = [User(created=datetime.now(), email="haha@gmail.com"), User(created=datetime.now(), email="exmple@gmail.com")]


session_maker = sessionmaker(bind=create_engine("mysql://todo_user:todo_pass@localhost:3306/todo_db"))

with session_maker() as session:
    for user in users:
        session.add(user)
    session.commit()


    