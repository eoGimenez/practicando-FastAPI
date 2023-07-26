from datetime import timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, Security, status
from sqlalchemy.orm import Session
from fastapi.security import (
    OAuth2PasswordRequestForm,
)
from schemas.user import UserBase, UserDisplay
from schemas.token import Token
from config.db import get_db
from config import db_auth


ACCESS_TOKEN_EXPIRE_MINUTES = 30


router = APIRouter(
    tags=['Authentication']
)


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
):
    user: UserBase = db_auth.authenticate_user(
        form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = db_auth.create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserDisplay)
async def read_users_me(
    current_user: Annotated[UserBase, Depends(db_auth.get_current_active_user)]
):
    return current_user


@router.get("/users/me/articles/")
async def read_own_items(
    current_user: Annotated[UserBase, Security(
        db_auth.get_current_active_user, scopes=["articles"])]
):
    items = []
    for item in current_user.items:
        items.append(item)
    return items


@router.get("/status/")
async def read_system_status(current_user: Annotated[UserBase, Depends(db_auth.get_current_user)]):
    return {
        "status": "ok",
        "current user": current_user
    }
