from pydantic import BaseModel, Field
from typing import Optional


class BookCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=200)
    author: str = Field(..., min_length=2, max_length=100)
    year: int = Field(..., ge=1900, le=2100)
    available: bool = True


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=2, max_length=200)
    author: Optional[str] = Field(None, min_length=2, max_length=100)
    year: Optional[int] = Field(None, ge=1900, le=2100)
    available: Optional[bool] = None


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    available: bool
