from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base


# SQLAlchemy model for User
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


# Pydantic models
class User(BaseModel):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str


class UserResponse(BaseModel):
    username: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
