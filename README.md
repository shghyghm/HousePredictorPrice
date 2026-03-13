# 🏠 HousePredictorPrice API

A **FastAPI-based backend** for managing houses and predicting house prices using **Machine Learning**.

This project demonstrates how to integrate:

* FastAPI
* JWT Authentication
* SQLAlchemy
* Scikit-learn

---

# 🚀 Features

* User **registration & login**
* **JWT authentication**
* Create and manage houses
* **House price prediction API**
* Interactive API docs with Swagger

---

# 🧠 Machine Learning

The API predicts house prices based on:

* Size
* Number of rooms
* Building age
* Location score

Model used:

```
RandomForestRegressor
```

---

# 📡 Main Endpoints

### Auth

```
POST /auth/register
POST /auth/login
```

### Houses

```
POST /houses
POST /houses/predict-price
```

Example request:

```json
{
  "size": 140,
  "rooms": 3,
  "age": 10,
  "location_score": 7
}
```

---

# ▶️ Run the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run server:

```
uvicorn app.main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

# 🛠 Tech Stack

* FastAPI
* Python
* SQLAlchemy
* SQLite
* Scikit-learn
* JWT
