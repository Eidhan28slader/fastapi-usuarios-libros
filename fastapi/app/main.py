from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="API de Usuarios y Libros",
    description="API CRUD para gestionar usuarios y libros.",
    version="1.0.0",
)


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


users_db: Dict[int, User] = {}
books_db: Dict[int, Book] = {}


def next_id(storage: Dict[int, object]) -> int:
    return max(storage.keys(), default=0) + 1


@app.get("/")
def read_root():
    return {
        "message": "API funcionando correctamente",
        "entidades": ["usuarios", "libros"],
        "endpoints": [
            "/users",
            "/users/{user_id}",
            "/books",
            "/books/{book_id}",
        ],
    }


@app.get("/users", response_model=List[User])
def list_users():
    return list(users_db.values())


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@app.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    user_id = next_id(users_db)
    new_user = User(id=user_id, name=user.name, email=user.email, active=user.active)
    users_db[user_id] = new_user
    return new_user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate):
    current_user = users_db.get(user_id)
    if current_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    update_data = user.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)

    users_db[user_id] = current_user
    return current_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    del users_db[user_id]
    return {"message": "Usuario eliminado correctamente"}


@app.get("/books", response_model=List[Book])
def list_books():
    return list(books_db.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = books_db.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return book


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    book_id = next_id(books_db)
    new_book = Book(
        id=book_id,
        title=book.title,
        author=book.author,
        year=book.year,
        available=book.available,
    )
    books_db[book_id] = new_book
    return new_book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate):
    current_book = books_db.get(book_id)
    if current_book is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    update_data = book.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_book, field, value)

    books_db[book_id] = current_book
    return current_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    del books_db[book_id]
    return {"message": "Libro eliminado correctamente"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
