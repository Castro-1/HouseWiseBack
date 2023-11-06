from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

class Features(BaseModel):
    status: str
    bed: float
    bath: float
    acre_lot: float
    city: str
    state: str
    zip_code: float
    house_size: float
    prev_sold_date: str


@app.get("/")
async def home():
    return {"health_check": "OK", "model_version": "1.0"}

@app.post("/")
async def predict(features: Features):
    return features