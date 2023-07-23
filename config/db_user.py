from sqlalchemy.orm.session import Session
from schemas.user import UserBase
from models.user import DbUser
from config.hash import Hash

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
    return db.query(DbUser).filter(DbUser.id == id).first()


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: hasher.bcrypt(request.password)
    })
    db.commit()
    return 'Updated'


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.delete(user)
    db.commit()
    return 'Usuario borrado'
