from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class JobCreate(BaseModel):
    title: str
    company: str
    status: Optional[str] = "Wishlist"
    url: Optional[str] = None

class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    status: str
    url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True
