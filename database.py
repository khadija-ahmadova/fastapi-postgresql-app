import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
database_url = os.getenv("DATABASE_URL")

# connects sqlalchemy to postgresql databse
engine = create_engine(database_url)

# db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for models to inherit
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
