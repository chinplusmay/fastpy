from fastapi import FastAPI
from pydantic import BaseModel
from app.routers.users import router

from app.databases.connection import engine
from app.models import user_model



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

user_model.Base.metadata.create_all(bind=engine)