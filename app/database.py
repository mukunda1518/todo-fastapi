from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import settings


# mysql
try:
    engine = create_engine(settings.MYSQL_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    pass

Base = declarative_base()

def get_mysql_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
