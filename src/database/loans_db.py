from typing import Optional
from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.books import Book
from src.models.loan import Loan, LoanUpdate
from src.models.users import User


def get_all_loans(db: Session):
    query = select(Loan)
    result = db.exec(query).all()
    return result


def get_all_loans_active(db: Session):
    query = select(Loan).where(Loan.returned == 0)
    result = db.exec(query).all()
    return result
