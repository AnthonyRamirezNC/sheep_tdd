from fastapi import FastAPI
from fastapi.testclient import TestClient 
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.getSheep(id)
    

