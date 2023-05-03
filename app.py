from fastapi import FastAPI

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
    1: { "name": "Bambang", "age": 20 },
    2: { "name": "Sarah", "age": 18 },
    3: { "name": "Surtiyem", "age": 13 },
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]