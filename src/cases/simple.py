"""
The simple application is kind a naive.

It has the following considerations:

1. Create the pydantic object manually.
2. Use _sync_ functions.
3. On the server, use the h11 HTTP implementations and asyncio event loop.
"""
from fastapi import FastAPI

from src.data import OUTPUT
from src.schemas import Output

app = FastAPI()


@app.get("/", response_model=list[Output])
def home():
    return [Output(**item) for item in OUTPUT]
