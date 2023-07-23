from sqlalchemy.orm.session import Session
from schemas.user import UserBase
from models.user import DbUser
from config.hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(Hash, password=request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
