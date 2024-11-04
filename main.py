from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# Define the Sheep model
class Sheep(BaseModel):
    id: int
    name: str
    age: int

# Simulated in-memory database
db = {
    "data": {}
}

# Create Sheep
@app.post(path="/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db["data"]:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")
    db["data"][sheep.id] = sheep
    return sheep

# Read all Sheep
@app.get(path="/sheep/", response_model=list[Sheep])
def get_all_sheep():
    return list(db["data"].values())

# Update Sheep
@app.put(path="/sheep/{sheep_id}", response_model=Sheep)
def update_sheep(sheep_id: int, updated_sheep: Sheep):
    if sheep_id not in db["data"]:
        raise HTTPException(status_code=404, detail="Sheep not found")
    db["data"][sheep_id] = updated_sheep
    return updated_sheep

# Delete Sheep
@app.delete(path="/sheep/{sheep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(sheep_id: int):
    if sheep_id not in db["data"]:
        raise HTTPException(status_code=404, detail="Sheep not found")
    del db["data"][sheep_id]
    return
