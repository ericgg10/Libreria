from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from src.database import book_db, db_session
from src.models.books import Book
from src.models.loan import Loan
from src.models.users import User

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def get_all_book(db: db_session):
    return book_db.get_all_books(db)


@router.get("/id/{id}")
def get_book_with_id(db: db_session, id: UUID):
    book = book_db.get_books_by_id(db, id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found with ID {id}"
        )
    return book
