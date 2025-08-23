from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from src.database import db_session, users_db
from src.models.books import Book
from src.models.loan import Loan
from src.models.users import User, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_all_users(db: db_session):
    return users_db.get_all_users(db)


@router.get("/{id}")
def get_users_by_id(db: db_session, id: UUID):
    user = users_db.get_user_by_id(db, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found with id {id}"
        )
    return user


@router.get("/{id}/loans")
def get_loans_users(db: db_session, user_id: UUID):
    loans = users_db.get_loans_user(db, user_id)
    if not loans:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No loans were found for this user",
        )
    return loans


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(db: db_session, user_info: UserCreate):
    new_user = User(**user_info.model_dump())
    created_user = users_db.create_user(db, new_user)
    return created_user


@router.patch("/{id}")
def update_user(db: db_session, id: UUID, new_user: UserUpdate):
    return users_db.update_user(db, id, new_user)


@router.delete("/{id}")
def delete_user(db: db_session, id: UUID):
    deleted_user = users_db.delete_user(db, id)
    return deleted_user
