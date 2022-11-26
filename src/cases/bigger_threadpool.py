import anyio
from fastapi import FastAPI

from src.data import OUTPUT
from src.schemas import Output


async def startup():
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = 100


app = FastAPI(on_startup=[startup])


@app.get("/", response_model=list[Output])
def home():
    return [Output(**item) for item in OUTPUT]
