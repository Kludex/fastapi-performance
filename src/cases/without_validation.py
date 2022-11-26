from fastapi import FastAPI

from src.data import OUTPUT

app = FastAPI()


@app.get("/")
def home():
    return OUTPUT
