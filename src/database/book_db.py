from typing import Optional
from uuid import UUID

from sqlmodel import Session, SQLModel, select

from src.database import engine
from src.models.books import Book
from src.models.loan import Loan
from src.models.users import User


def get_all_books(db: Session):
    query = select(Book)
    result = db.exec(query).all()
    return result


def get_books_by_id(db: Session, book_id: int):
    return db.get(Book, book_id)


def get_loans_book(db: Session, book_id: UUID):
    query = select(Loan).where(Loan.book_id == book_id)
    result = db.exec(query).all()
    return result


def get_books_attribute(
    db: Session,
    title: Optional[str] = None,
    author: Optional[str] = None,
    genre: Optional[str] = None,
    limit: int = 10,
):
    query = select(Book)

    if title:
        query = query.where(Book.title == title)
    if author:
        query = query.where(Book.author == author)
    if genre:
        query = query.where(Book.genre == genre)
    query = query.limit(limit)
    result = db.exec(query).all()
    return result
