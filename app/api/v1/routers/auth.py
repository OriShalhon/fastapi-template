from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import models
from app.schemas import schemas
from app.utils import oauth2, utils

router = APIRouter(
    tags=["authentications"],
)


@router.post("/login", response_model=schemas.Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    found_user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )

    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User not found"
        )  # change the details to "Invalid credentials"

    if not utils.verify_password(user_credentials.password, found_user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect password"
        )  # change the details to "Invalid credentials"

    # here we generate a jwt token
    access_token = oauth2.create_access_token(
        data={"user_email": found_user.email, "user_id": found_user.id}
    )

    return {"access_token": access_token, "token_type": "bearer"}


1
