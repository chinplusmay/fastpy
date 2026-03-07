from fastapi import FastAPI
from pydantic import BaseModel
from app.routers.users import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"msg" : "Hello"}


@app.get("/search")
def search(q : str):
    return {"query": q}

@app.get("/products")
def products(limit : int = 10, size : int = 0):
    return {"limit": limit, "size" : size}
