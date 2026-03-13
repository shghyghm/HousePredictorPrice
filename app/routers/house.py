from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..services.security import get_current_user
from ..services.ml_model import predict_price

router = APIRouter(
    prefix="/houses",
    tags=["Houses"]
)


@router.post("/")
def create_house(
    house: schemas.HouseCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_house = models.House(
        title=house.title,
        price=house.price,
        description=house.description,
        owner_id=current_user.id,
        size=house.size,
        rooms=house.rooms,
        age=house.age,
        location_score=house.location_score,
    )

    db.add(new_house)
    db.commit()
    db.refresh(new_house)

    return new_house

@router.get("/", response_model=list[schemas.HouseResponse])
def get_my_houses(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    houses = db.query(models.House).filter(
        models.House.owner_id == current_user.id
    ).all()

    return houses



@router.get("/{house_id}", response_model=schemas.HouseResponse)
def get_house(
    house_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    house = db.query(models.House).filter(models.House.id == house_id).first()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    
    if house.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to view this house")
    
    return house


@router.delete("/{house_id}")
def delete_house(
    house_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)  # اینجا JWT کاربر
):
    house = db.query(models.House).filter(models.House.id == house_id).first()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    
    if house.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this house")
    
    db.delete(house)
    db.commit()
    return {"detail": "House deleted successfully"}


@router.post("/predict-price")
def predict_house_price(
    data: schemas.HousePrediction,
    db: Session = Depends(get_db)
):

    price = predict_price(
        db,
        data.size,
        data.rooms,
        data.age,
        data.location_score
    )

    if price is None:
        raise HTTPException(
            status_code=400,
            detail="Not enough data to train model"
        )

    return {"predicted_price": price}