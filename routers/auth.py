import os
from datetime import datetime, timedelta
from passlib.context import CryptContext
import jwt
from fastapi import APIRouter, Depends, Security, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from config.db import get_db
from models import tables
from schemas.user import UserLogin, UserBase
from dotenv import load_dotenv
load_dotenv()

router = APIRouter(
    tags=['authentication']
)


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
    secret = os.environ.get("SECRET")

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_passdword):
        return self.pwd_context.verify(plain_password, hashed_passdword)

    def encode_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Signature has expired') from exc
        except jwt.InvalidTokenError as inv:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Invalid credentiasl - from jwn, dev mode comment') from inv

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


auth_handler = AuthHandler()


@router.post('/token')
def get_token(request: UserLogin, db: Session = Depends(get_db)):
    user = db.query(tables.DbUser).filter(
        tables.DbUser.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Ivalid credentials')
    # if not auth_handler.verify_password(user.password, request.password):
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail='Ivalid credentials')
    access_token = auth_handler.encode_token(user.id)
    return {
        "access_token": access_token,
        "token_type": 'Bearer',
        'user_id': user.id,
        'username': user.username
    }
