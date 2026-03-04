from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..services.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token({"sub": db_user.username})

    return {"access_token": access_token, "token_type": "bearer"}