from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Task
from datetime import datetime


users = [User(created=datetime.now(), email="haha@gmail.com"), User(created=datetime.now(), email="exmple@gmail.com")]


session_maker = sessionmaker(bind=create_engine("sqlite:///database.db"))

with session_maker() as session:
    for user in users:
        session.add(user)
    session.commit()


    