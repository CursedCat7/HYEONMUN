from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Codespaces + FastAPI 🚀"}

class User(BaseModel):
    name: str
    age: int

def test(self):
    pass

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created!", "user": user}