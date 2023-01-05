
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
    db_driver = models.driver(driver_name=driver.driver_name,race_number=driver.race_number, country=driver.country)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def get_driver_by_name(db: Session, driver_name:str):
    return db.query(models.driver).filter(models.driver.driver_name == driver_name).first()

def create_team(db: Session, team: schemas.teamCreate):
    db_team = models.team(team_name=team.team_name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def create_circuit(db: Session, circuit: schemas.circuitCreate):
    db_circuit = models.circuit(circuit_name=circuit.circuit_name)
    db.add(db_circuit)
    db.commit()
    db.refresh(db_circuit)
    return db_circuit


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()