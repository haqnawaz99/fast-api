from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to FastAPI Series !"


@app.get("/contact")
def contact():
    return "You can connect us any time."
