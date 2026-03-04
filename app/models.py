from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    houses = relationship("House", back_populates="owner")


class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    area = Column(Float)
    price = Column(Float)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="houses")