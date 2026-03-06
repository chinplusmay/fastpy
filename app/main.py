from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

@app.get("/")
def home():
    return {"msg" : "Hello"}

@app.get("/users/{user_id}")
def getUser(user_id : int):
    return {"user_id" : user_id}

@app.get("/search")
def search(q : str):
    return {"query": q}

@app.get("/products")
def products(limit : int = 10, size : int = 0):
    return {"limit": limit, "size" : size}



class User(BaseModel):
    name :str
    age :int

@app.post("/users") 
def create_user(user: User):
    return {"user": user}