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
    description: Optional[str] = None
    bedrooms: int
    bathrooms: int
    area: float


class HouseCreate(HouseBase):
    pass


class HouseOut(HouseBase):
    id: int
    price: float
    owner_id: int

    class Config:
        from_attributes = True