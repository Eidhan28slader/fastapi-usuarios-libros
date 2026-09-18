from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., min_length=5, max_length=150)
    active: bool = True


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[str] = Field(None, min_length=5, max_length=150)
    active: Optional[bool] = None


class User(BaseModel):
    id: int
    name: str
    email: str
    active: bool
