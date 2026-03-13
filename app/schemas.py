from pydantic import BaseModel
from typing import Optional



class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True



class HouseBase(BaseModel):
    title: str
    price: float
    description: str


class HouseCreate(BaseModel):
    title: str
    description: str
    size: float
    rooms: int
    age: int
    location_score: float
    price: float


class HouseResponse(HouseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class HousePrediction(BaseModel):
    size: float
    rooms: int
    age: int
    location_score: float