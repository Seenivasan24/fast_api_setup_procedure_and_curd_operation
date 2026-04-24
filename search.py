from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search_item(
    name: str,
    age: int,
    blood_group: str,
    city: str,
    phone: int
):
    return {
        "name": name,
        "age": age,
        "blood_group": blood_group,
        "city": city,
        "phone": phone
    }