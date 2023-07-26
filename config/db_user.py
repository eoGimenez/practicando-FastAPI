from sqlalchemy.orm.session import Session
from schemas.user import UserBase
from models.tables import DbUser
from config.hash import Hash
from fastapi import HTTPException, status

hasher = Hash()


def create_user(db: Session, request: UserBase):

    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=hasher.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id {id}, not found')
    return user


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id {username}, not found')
    return user


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id {id}, not found')
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: hasher.bcrypt(request.password)
    })
    db.commit()
    return 'Updated'


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id {id}, not found')
    user.delete(user)
    db.commit()
    return 'Usuario borrado'
