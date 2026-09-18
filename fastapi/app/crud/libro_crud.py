from typing import List, Optional

from app.schemas.book import BookCreate, BookUpdate, Book
from app.services.storage import books_db, next_id


def list_books() -> List[Book]:
    return list(books_db.values())


def get_book(book_id: int) -> Optional[Book]:
    return books_db.get(book_id)


def create_book(book_in: BookCreate) -> Book:
    book_id = next_id(books_db)
    book = Book(id=book_id, **book_in.model_dump())
    books_db[book_id] = book
    return book


def update_book(book_id: int, book_in: BookUpdate) -> Optional[Book]:
    current = books_db.get(book_id)
    if not current:
        return None
    update_data = book_in.model_dump(exclude_unset=True)
    updated = current.model_copy(update=update_data)
    books_db[book_id] = updated
    return updated


def delete_book(book_id: int) -> bool:
    if book_id in books_db:
        del books_db[book_id]
        return True
    return False
