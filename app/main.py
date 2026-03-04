from fastapi import FastAPI
from .database import engine, Base
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HousePredictorPrice API")


@app.get("/")
def root():
    return {"message": "Welcome to HousePredictorPrice"}