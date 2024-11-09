import os
from datetime import datetime, timedelta

from jose import JWTError, jwt

# for the toekn there are 3 required parameters
# 1. secret key
# 2. algorithm
# 3. expiration time

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("EXPIRATION_TIME"))


# this function is used to create a jwt token
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    # this is used to set the expiration time
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
