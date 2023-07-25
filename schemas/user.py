from pydantic import BaseModel
from typing import List
from schemas.article import Article


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    class Config():
        from_attributes = True
