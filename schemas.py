from pydantic import BaseModel
from typing import Optional


class CollegeBase(BaseModel):
    name: str
    address: str | None = None
    city: str | None = None
    state: str | None = None
    location: str | None = None
    type: str | None = None
    established: int | None = None
    website: str | None = None
    description: str | None = None

class CollegeCreate(CollegeBase):
    pass

class CollegeUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    established_year: Optional[int] = None


class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    username: str
    password: str
    role: str  # Either "user" or "admin"