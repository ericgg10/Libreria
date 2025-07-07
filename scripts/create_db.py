import uuid
from datetime import datetime

import pandas as pd
from sqlmodel import Session, SQLModel, select

from src.database import engine
from src.models.books import Book
from src.models.loan import Loan
from src.models.users import User

books = pd.read_csv("data/books.csv")
users = pd.read_csv("data/users.csv")
loans = pd.read_csv("data/loans.csv")


def create_tables():
    SQLModel.metadata.create_all(engine)


def parse_date(date_str):
    if pd.isna(date_str) or not date_str:
        return None
    return datetime.strptime(date_str, "%d-%m-%Y").date()


def insert_values():
    with Session(engine) as session:
        user_ids = []
        books_ids = []

        for _, row in books.iterrows():
            book = session.exec(select(Book).filter_by(title=row["Title"])).first()
            if not book:
                book = Book(
                    title=row["Title"],
                    author=row["Author"],
                    year=row["Year"],
                    genre=row["Genre"],
                    isbn=row["Isbn"],
                    copies=row["Copies"],
                )
                session.add(book)
                session.flush()
            books_ids.append(book.id)

        for _, row in users.iterrows():
            user = session.exec(select(User).filter_by(username=row["Username"])).first()
            if not user:
                user = User(
                    username=row["Username"],
                    password=row["Password"],
                    phone=row["Phone"],
                )
                session.add(user)
                session.flush()
            user_ids.append(user.id)

        for _, row in loans.iterrows():
            user_idx = int(row["User_Rank"]) - 1
            book_idx = int(row["Book_Rank"]) - 1
            print("User_Rank:", row["User_Rank"], "Book_Rank:", row["Book_Rank"])

            if user_idx < len(user_ids) and book_idx < len(books_ids):
                loan = Loan(
                    id=row["Loan_Rank"],
                    user_id=user_ids[user_idx],  # <- corregido
                    book_id=books_ids[book_idx],  # <- corregido
                    loan_date=parse_date(row["Loan_Date"]),
                    return_date=parse_date(row["Return_Date"])
                    if pd.notna(row["Return_Date"])
                    else None,
                    loan_days=row["Loan_Days"] if pd.notna(row["Loan_Days"]) else None,
                    returned=row["Returned"],
                )
                session.add(loan)
            else:
                print(f"[ERROR] Índices fuera de rango: user_idx={user_idx}, book_idx={book_idx}")

        session.commit()
        print("✅ Préstamos insertados exitosamente.")


def main():
    create_tables()
    insert_values()


if __name__ == "__main__":
    main()
