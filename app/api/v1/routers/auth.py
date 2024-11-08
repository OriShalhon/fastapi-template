from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas import schemas
from app.models import models
from app.utils import utils

router = APIRouter(
    tags=["authentications"],
)


@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    found_user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.email)
        .first()
    )

    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )  # change the details to "Invalid credentials"

    if not utils.verify_password(user_credentials.password, found_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password"
        )  # change the details to "Invalid credentials"

    # here we generate a jwt token
    return {"data": "login successful"}
1