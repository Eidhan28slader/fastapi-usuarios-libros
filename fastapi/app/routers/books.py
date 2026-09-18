from typing import List
from fastapi import APIRouter, HTTPException

from app.schemas.book import BookCreate, BookUpdate, Book
from app.crud.libro_crud import (
    list_books as crud_list_books,
    get_book as crud_get_book,
    create_book as crud_create_book,
    update_book as crud_update_book,
    delete_book as crud_delete_book,
)

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=List[Book])
def list_books():
    return crud_list_books()


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = crud_get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return book


@router.post("/", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    return crud_create_book(book)


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate):
    updated = crud_update_book(book_id, book)
    if updated is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return updated


@router.delete("/{book_id}")
def delete_book(book_id: int):
    ok = crud_delete_book(book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"message": "Libro eliminado correctamente"}
