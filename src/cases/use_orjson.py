from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.data import OUTPUT
from src.schemas import Output

app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/", response_model=list[Output])
async def home():
    return OUTPUT
