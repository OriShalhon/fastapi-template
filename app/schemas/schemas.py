# this file could be seperated into multiple files, but for simplicity I have kept it in one file for the tamplate

from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
