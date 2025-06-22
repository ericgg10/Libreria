from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hola desde la librería creada por Eric García"}

