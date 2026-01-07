from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int
    tax: Optional[float] = None

@app.get("/")
async def read_root():
    return {"message": "This is day 2 of learning."}