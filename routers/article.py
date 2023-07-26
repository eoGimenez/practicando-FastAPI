from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from schemas.article import ArticleBase, ArticleDisplay
from config.db import get_db
from config import db_article
from schemas.token import TokenData
from config.db_auth import get_current_active_user


router = APIRouter(
    prefix='/article',
    tags=['article']
)


@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), token: TokenData = Security(get_current_active_user, scopes=["articles"])):
    return db_article.create_article(db, request)


@router.get('/{id}', response_model=ArticleDisplay)
def get_artivle(id: int, db: Session = Depends(get_db), token: TokenData = Security(get_current_active_user, scopes=["articles"])):
    return db_article.get_article(db, id)
