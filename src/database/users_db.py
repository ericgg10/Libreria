from uuid import UUID

from sqlmodel import Session, SQLModel, select

from src.database import engine
from src.models.books import Book
from src.models.loan import Loan
from src.models.users import User


def get_all_users(db: Session):
    query = select(User)
    result = db.exec(query).all()
    return result


def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)


def get_loans_user(db: Session, user_id: UUID):
    query = select(Loan).where(Loan.user_id == user_id)
    result = db.exec(query).all()
    return result


def create_user(db: Session, user_info: User):
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return user_info


def update_user(db: Session, user_id: UUID, new_user: User):
    query = select(User).where(User.id == user_id)
    old_user = db.exec(query).first()
    old_user.username = new_user.username if new_user.username else old_user.username
    old_user.password = new_user.password if new_user.password else old_user.password
    old_user.phone = new_user.phone if new_user.phone else old_user.phone

    db.commit()
    db.refresh(old_user)
    return old_user


def delete_user(db: Session, user_id):
    query = select(User).where(User.id == user_id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
    return result
