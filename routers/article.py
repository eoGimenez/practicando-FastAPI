from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.article import ArticleBase, ArticleDisplay
from config.db import get_db
from config import db_article
from typing import List
from auth.oauth2 import oauth2_schema


router = APIRouter(
    prefix='/article',
    tags=['article']
)


@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get('/{id}', response_model=ArticleDisplay)
def get_artivle(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    return db_article.get_article(db, id)
