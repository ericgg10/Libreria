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
