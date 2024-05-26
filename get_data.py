from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Task
from datetime import datetime

session_maker = sessionmaker(bind=create_engine("sqlite:///database.db"))

with session_maker() as session:
    users = session.query(User).all()
    for user in users:
        print(user.dict())
        
