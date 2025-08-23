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


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_loans(db: db_session, loan_info: LoanCreate):
    user = db.exec(select(User).where(User.username == loan_info.user_name)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")

    book = db.exec(select(Book).where(Book.title == loan_info.book_title)).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found book")

    copies_left = book.copies
    if copies_left < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No copies left")
    new_loan = Loan(
        user_id=user.id,
        book_id=book.id,
        loan_date=loan_info.loan_date,
        loan_days=loan_info.loan_days,
        returned=False,
    )

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    return new_loan


@router.patch("/{id}")
def update_loans(db: db_session, id: int, new_loan: LoanUpdate):
    return loans_db.update_loans(db, id, new_loan)
