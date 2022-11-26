from fastapi import FastAPI

from src.data import OUTPUT
from src.schemas import Output

app = FastAPI()


@app.get("/", response_model=list[Output])
def home():
    return OUTPUT
