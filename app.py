from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"response": "hello, world!"}

@app.get("/about")
def about():
    return {"response": "about"}
    