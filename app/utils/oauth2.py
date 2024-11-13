import os
from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import models
from app.schemas import schemas
from app.core.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# for the toekn there are 3 required parameters
# 1. secret key
# 2. algorithm
# 3. expiration time

SECRET_KEY = settings.jwt_secret_key
ALGORITHM = settings.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.jwt_expiration_time_minutes


# this function is used to create a jwt token
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    # this is used to set the expiration time
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credential_exception) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if not user_id:
            raise credential_exception
        token_data = schemas.TokenData(id=user_id)
    except JWTError:
        raise credential_exception

    return token_data


# this function should be used as a dependency for each route that requires authentication of the user
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> models.User:
    print(f"the token is {token}")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    found_token = verify_token(token, credentials_exception)

    logged_user = db.query(models.User).filter(models.User.id == found_token.id).first()

    return logged_user
