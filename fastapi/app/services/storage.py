from typing import Dict

from app.schemas.user import User
from app.schemas.book import Book


users_db: Dict[int, User] = {}
books_db: Dict[int, Book] = {}


def next_id(storage: Dict[int, object]) -> int:
    return max(storage.keys(), default=0) + 1
