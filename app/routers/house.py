from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..services.security import get_current_user

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
        owner_id=current_user.id
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