# models.py

from pydantic import BaseModel, HttpUrl
from typing import Optional
from sqlalchemy import Column, Integer, String
from database import Base 

class College(BaseModel):
    id: str
    name: str
    location: str
    type: str
    established: int
    website: HttpUrl
    description: Optional[str] = None

class CollegeCreate(BaseModel):
    name: str
    location: str
    type: str
    established: int
    website: HttpUrl
    description: Optional[str] = None

class CollegeUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    type: Optional[str] = None
    established: Optional[int] = None
    website: Optional[HttpUrl] = None
    description: Optional[str] = None


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True)
    password: str = Column(String)
    role: str = Column(String)


from sqlalchemy import Column, String, Integer
from database import Base

class College(Base):
    __tablename__ = "colleges"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    established = Column(Integer)
    location = Column(String)
    website = Column(String)
    type = Column(String)         # Already added
    description = Column(String) # ✅ New column added

