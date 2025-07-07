from typing import Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, status

from src.database import book_db, db_session
from src.models.books import Book
from src.models.loan import Loan
from src.models.users import User

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def get_all_book(db: db_session):
    return book_db.get_all_books(db)


@router.get("/search")
def get_books_attributes(
    db: db_session,
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    genre: Optional[str] = Query(None),
    limit: int = 10,
):
    book = book_db.get_books_attribute(db, title=title, author=author, genre=genre, limit=limit)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No books were found with these attributes",
        )
    return book


@router.get("/{id}")
def get_book_with_id(db: db_session, id: UUID):
    book = book_db.get_books_by_id(db, id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found with ID {id}"
        )
    return book


@router.get("/{id}/loans")
def get_loans_books(db: db_session, book_id: UUID):
    loans = book_db.get_loans_book(db, book_id)
    if not loans:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No loans were found for this book",
        )
    return loans
