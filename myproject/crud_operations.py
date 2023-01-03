from sqlalchemy.orm import Session
import auth
import models
import schemas


def get_driver(db: Session, driver_id: int):
    return db.query(models.driver).filter(models.driver.driver_id == driver_id).first()



def get_circuit(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.circuit).offset(skip).limit(limit).all()


def get_team(db: Session, team: str):
    return db.query(models.team).filter(models.team.team_name ==team).first()


def get_all_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.driver).offset(skip).limit(limit).all()

def get_all_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.team).offset(skip).limit(limit).all()


def create_driver(db: Session, driver: schemas.driverCreate):
    db_driver = models.driver(driver_name=driver.driver_name,race_number=driver.race_number, country= driver.country)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def get_driver_by_name(db: Session, driver_name:str):
    return db.query(models.driver).filter(models.driver.driver_name == driver_name).first()


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
