from typing import List
from fastapi import APIRouter, HTTPException

from app.schemas.user import UserCreate, UserUpdate, User
from app.crud.usuario_crud import (
    list_users as crud_list_users,
    get_user as crud_get_user,
    create_user as crud_create_user,
    update_user as crud_update_user,
    delete_user as crud_delete_user,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[User])
def list_users():
    return crud_list_users()


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = crud_get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.post("/", response_model=User, status_code=201)
def create_user(user: UserCreate):
    return crud_create_user(user)


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate):
    updated = crud_update_user(user_id, user)
    if updated is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated


@router.delete("/{user_id}")
def delete_user(user_id: int):
    ok = crud_delete_user(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado correctamente"}
