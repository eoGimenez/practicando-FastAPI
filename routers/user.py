from fastapi import APIRouter, Depends
from schemas.user import UserBase, UserDisplay
from sqlalchemy.orm import Session
from config.db import get_db
from config import db_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
