from typing import Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from src.database import db_session, loans_db
from src.models.books import Book
from src.models.loan import Loan, LoanCreate, LoanUpdate
from src.models.users import User

router = APIRouter(prefix="/loans", tags=["Loans"])


@router.get("/")
def get_all_loans(db: db_session):
    return loans_db.get_all_loans(db)


@router.get("/active")
def get_all_loans_active(db: db_session):
    loans = loans_db.get_all_loans_active(db)
    if not loans:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not found any activate Loan"
        )
    return loans
