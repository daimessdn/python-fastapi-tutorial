from fastapi import FastAPI, Path

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
users = {
    1: {"name": "Bambang", "age": 20},
    2: {"name": "Sarah", "age": 18},
    3: {"name": "Surtiyem", "age": 13},
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]

# Using Path method in FastAPI
# Import Path first from fastapi module


@app.get("/users-2/{user_id}")
def get_user_2(user_id: int = Path(description="ID of user for wiewing user details.", gt=0, lt=4)):
    return users[user_id]
