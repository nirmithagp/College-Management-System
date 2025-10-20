from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

DATABASE_URL = os.getenv("DATABASE_URL")  # For example: "postgresql://postgres:password@localhost/yourdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()  # ✅ This must come AFTER engine, not from any other module

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




