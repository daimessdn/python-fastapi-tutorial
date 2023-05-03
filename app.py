from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

# init FastAPI instance
app = FastAPI()

# Adding route of GET endpoints


@app.get("/")
def index():
    return {"response": "hello, world!"}

@app.get("/about")
def about():
    return {"response": "about"}

# Working with parameters
users = {}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]

# Using Path method in FastAPI
# Import Path first from fastapi module

@app.get("/users-2/{user_id}")
def get_user_2(user_id: int = Path(description="ID of user for wiewing user details.", gt=0, lt=len(users))):
    return users[user_id]

# Working in queries
@app.get("/users-3")
def get_user_3(*, name: Optional[str] = None, test: int = None):
    for user_id in users:
        if users[user_id]["name"] == name:
            return { "user": users[user_id], "test": test }
        
    return { "response": "404 not found" }

# working with POST method
@app.post("/users/{user_id}")
def create_user(*, user_id: int = len(users) + 1, user: User):
    if user_id in users:
        return { "error": "user already exists" }
    
    users[user_id] = {
        "name": user.name,
        "age": user.age,
        "email": user.email
    }
    return users[user_id]

# working with PUT method
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        return { "error": "user no exists" }
    
    if user.name != None:
        users[user_id].name = user.name

    if user.age != None:
        users[user_id].age = user.age

    if user.email != None:
        users[user_id].email = user.email

    return users[user_id]

# working with DELETE method
@app.delete("/users/")
def delete_user(user_id: int = Query(..., description="The ID of user desired to be deleted")):
    if user_id not in users:
        return { "error": "user no exists" }
    
    del users[user_id]
    return { "response": "user deleted" }