from fastapi import FastAPI

from src.routes import book, loan, user

app = FastAPI()

app.include_router(book.router)
app.include_router(loan.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return {"Hola desde la librería creada por Eric García"}
