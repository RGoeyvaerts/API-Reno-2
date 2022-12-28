from sqlalchemy.orm import Session
import auth
import models
import schemas


def get_driver(db: Session, driver_name:str):
    return db.query(models.driver).filter(models.driver.driver_name == driver_name).first()


def get_team(db: Session, team: str):
    return db.query(models.team).filter(models.team.team_name ==team).first()


def get_all_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.driver).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     hashed_password = auth.get_password_hash(user.password)
#     db_user = models.User(email=user.email, hashed_password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
