from pydantic import BaseModel
from typing import List
from schemas.article import Article


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    active: bool = True


class UserLogin(BaseModel):
    username: str
    password: str
    activa: bool


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    active: bool

    class Config():
        from_attributes = True
