from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.books import Book
from src.models.loan import Loan, LoanPublic
from src.models.users import User


def get_all_loans(db: Session):
    query = (
        select(Loan, Book.title, User.username)
        .where(Loan.book_id == Book.id)
        .where(Loan.user_id == User.id)
    )
    result = db.exec(query).all()

    list_of_results = []

    for single_result in result:
        loan, book_title, username = single_result
        loan_public = LoanPublic(**loan.model_dump(), book_title=book_title, username=username)
        list_of_results.append(loan_public)

    return list_of_results


def get_all_loans_active(db: Session):
    query = select(Loan).where(Loan.returned == 0)
    result = db.exec(query).all()
    return result


def create_loans(db: Session, loan_info: Loan):
    db.add(loan_info)
    db.commit()
    db.refresh(loan_info)
    return loan_info


def update_loans(db: Session, loan_id: int, new_loan: Loan):
    query = select(Loan).where(Loan.id == loan_id)
    old_loan = db.exec(query).first()

    if new_loan is not None:
        old_loan.returned = new_loan.returned
    db.commit()
    db.refresh(old_loan)
    return old_loan
