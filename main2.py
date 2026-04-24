from fastapi import FastAPI

app = FastAPI()

@app.get("/seenivasan")
def home():
    return {"message": "Hello from main2"}