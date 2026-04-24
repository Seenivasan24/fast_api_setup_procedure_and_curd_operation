
from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}")
def get_name(name: str):
    return {"message": f"Hello {name}"}

#run this http://127.0.0.1:8001/seenivasan 
#output {"message":"Hello seenivasan "}