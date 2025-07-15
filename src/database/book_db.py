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


def create_book(db: Session, book_info: Book):
    db.add(book_info)
    db.commit()
    db.refresh(book_info)
    return book_info


def update_book(db: Session, new_book: Book):
    query = select(Book).where(Book.id == new_book.id)
    old_book = db.exec(query).first()
    old_book.title = new_book.title if new_book.title else old_book.title
    old_book.author = new_book.author if new_book.author else old_book.author
    old_book.year = new_book.year if new_book.year else old_book.year
    old_book.genre = new_book.genre if new_book.genre else old_book.genre
    old_book.isbn = new_book.isbn if new_book.isbn else old_book.isbn
    old_book.copies = new_book.copies if new_book.copies else old_book.copies

    db.commit()
    db.refresh(old_book)
    return old_book


def delete_book(db: Session, book_id):
    query = select(Book).where(Book.id == book_id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
    return result
