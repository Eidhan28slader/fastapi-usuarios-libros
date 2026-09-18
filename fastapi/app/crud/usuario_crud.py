from typing import List, Optional

from app.schemas.user import UserCreate, UserUpdate, User
from app.services.storage import users_db, next_id


def list_users() -> List[User]:
    return list(users_db.values())


def get_user(user_id: int) -> Optional[User]:
    return users_db.get(user_id)


def create_user(user_in: UserCreate) -> User:
    user_id = next_id(users_db)
    user = User(id=user_id, **user_in.model_dump())
    users_db[user_id] = user
    return user


def update_user(user_id: int, user_in: UserUpdate) -> Optional[User]:
    current = users_db.get(user_id)
    if not current:
        return None
    update_data = user_in.model_dump(exclude_unset=True)
    updated = current.model_copy(update=update_data)
    users_db[user_id] = updated
    return updated


def delete_user(user_id: int) -> bool:
    if user_id in users_db:
        del users_db[user_id]
        return True
    return False
