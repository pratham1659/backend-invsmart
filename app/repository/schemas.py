from typing import Optional
from pydantic import BaseModel


class BookCreateModel(BaseModel):
    title: str
    author: str


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    rating: Optional[int] = None


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
    rating: Optional[int] = None
