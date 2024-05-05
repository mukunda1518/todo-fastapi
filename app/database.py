from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

session_maker = sessionmaker(bind=create_engine("sqlite:///database.db"))
