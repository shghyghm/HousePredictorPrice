from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import auth, house

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HousePredictorPrice API")

app.include_router(auth.router)
app.include_router(house.router)

@app.get("/")
def root():
    return {"message": "Welcome to HousePredictorPrice"}