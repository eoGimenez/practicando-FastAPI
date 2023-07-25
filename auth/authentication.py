# from fastapi import APIRouter, Depends, HTTPException, status
# # from fastapi.param_functions import Depends
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from config.db import get_db
# from config.hash import Hash
# from models import tables
# from auth import oauth2
# from typing import Optional


# router = APIRouter(
#     tags=['authentication']
# )

# hasher = Hash()


# @router.post('/token')
# def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(tables.DbUser).filter(
#         tables.DbUser.username == request.username).first()
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail='Ivalid credentials')
#     if not hasher.verify(user.password, request.password):
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail='Ivalid credentials')
#     access_token = oauth2.create_access_token(data={'sub': user.username})
#     print(access_token)
#     return {
#         "access_token": access_token,
#         'token_type': 'bearer',
#         'user_id': user.id,
#         'username': user.username
#     }
