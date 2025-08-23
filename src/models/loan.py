import uuid
from datetime import date
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.models.books import Book
from src.models.users import User


class Loan(SQLModel, table=True):
    id: int = Field(primary_key=True)

    user_id: uuid.UUID = Field(foreign_key="user.id")
    user: User = Relationship()

    book_id: uuid.UUID = Field(foreign_key="book.id")
    book: Book = Relationship()

    loan_date: Optional[date]
    return_date: Optional[date]
    loan_days: Optional[int]
    returned: bool


class LoanUpdate(SQLModel):
    id: int
    returned: Optional[bool] = None


class LoanCreate(SQLModel):
    user_name: Optional[str] = None
    book_title: Optional[str] = None
    loan_date: Optional[date] = None
    return_date: Optional[date] = None
    loan_days: Optional[int] = None
    returned: Optional[bool] = None
