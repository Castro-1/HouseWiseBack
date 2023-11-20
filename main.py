from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model.model import predictPrice
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

class Features(BaseModel):
    status: float
    bed: float
    bath: float
    acre_lot: float
    city: float
    state: float
    zip_code: float
    house_size: float
    prev_sold_date: float

def convertFeatures(features):
    status, bed, bath, acre_lot, city, state, zip_code, house_size, prev_sold_date = features.status, features.bed, features.bath, features.acre_lot, features.city, features.state, features.zip_code, features.house_size, features.prev_sold_date
    return np.array([status, bed, bath, acre_lot, city, state, zip_code, house_size, prev_sold_date])


@app.get("/")
async def home():
    return {"health_check": "OK", "model_version": "1.0"}

@app.post("/")
async def predict(features: Features):
    features = convertFeatures(features)
    return predictPrice(features)