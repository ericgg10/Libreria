import uuid

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str
    password: str
    phone: str


class UserUpdate(SQLModel):
    id: uuid.UUID
    username: str
    password: str
    phone: str


class UserCreate(SQLModel):
    username: str
    password: str
    phone: str
