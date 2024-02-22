from fastapi import FastAPI
from db.repo import Repository

app = FastAPI()

@app.get("/")
async def check():
    return {"stats": "ok"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    repo = Repository()
    return repo.get_item(item_id)
