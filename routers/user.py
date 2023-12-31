from typing import List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from schemas.user import UserBase, UserDisplay
from config.db import get_db
from config import db_user
from schemas.token import TokenData
from config.db_auth import get_current_active_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get('/', response_model=List[UserDisplay])
def get_users(db: Session = Depends(get_db), token: TokenData = Security(get_current_active_user, scopes=["me"])):
    return db_user.get_all_users(db)


@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db), token: TokenData = Security(get_current_active_user, scopes=["me"])):
    return db_user.get_user(db, id)


@router.put('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db), token: TokenData = Security(get_current_active_user, scopes=["me"])):
    return db_user.update_user(db, id, request)


@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db), token: TokenData = Security(get_current_active_user, scopes=["me"])):
    return db_user.delete_user(db, id)
