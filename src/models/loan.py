import uuid

from sqlmodel import Field, Relationship, SQLModel

from src.models.books import Book
from src.models.users import User


class Loan(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    user_id: uuid.UUID = Field(foreign_key="user.id")
    user: User = Relationship()

    book_id: uuid.UUID = Field(foreign_key="book.id")
    book: Book = Relationship()

    loan_date: int
    return_date: int
    loan_days: int
    returned: bool
