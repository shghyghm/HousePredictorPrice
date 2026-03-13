import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sqlalchemy.orm import Session
from .. import models


def train_model(db: Session):

    houses = db.query(models.House).all()

    if len(houses) < 5:
        return None

    X = []
    y = []

    for house in houses:
        X.append([
            house.size,
            house.rooms,
            house.age,
            house.location_score
        ])

        y.append(house.price)

    X = np.array(X)
    y = np.array(y)

    model = RandomForestRegressor()

    model.fit(X, y)

    return model


def predict_price(db: Session, size, rooms, age, location_score):

    model = train_model(db)

    if model is None:
        return None

    features = np.array([[size, rooms, age, location_score]])

    prediction = model.predict(features)

    return float(prediction[0])