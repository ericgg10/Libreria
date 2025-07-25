import uuid

from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    author: str
    year: int
    genre: str
    isbn: str
    copies: int


class BookUpdate(SQLModel):
    id: uuid.UUID
    title: str
    author: str
    year: int
    genre: str
    isbn: str
    copies: int


class BookCreate(SQLModel):
    title: str
    author: str
    year: int
    genre: str
    isbn: str
    copies: int
