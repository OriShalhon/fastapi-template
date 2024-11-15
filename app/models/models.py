# this file could be seperated into multiple files, but for simplicity I have kept it in one file for the tamplate

# here wee define the structure of the db tabbles and the relationships between them

from sqlalchemy import Column, Integer, String

# from sqlalchemy.orm import relationship common to use in the models
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
