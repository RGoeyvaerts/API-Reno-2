from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import os
import crud_operations
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()
origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "https://rgoeyvaerts.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/drivers/", response_model=schemas.driver)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


@app.get("/drivers/", response_model=list[schemas.driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = crud_operations.get_all_drivers(db, skip=skip, limit=limit)
    return drivers


@app.get("/teams/", response_model=list[schemas.team])
def get_all_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = crud_operations.get_all_teams(db, skip=skip, limit=limit)
    return teams

@app.get("/circuit/", response_model=list[schemas.circuit])
def read_circuit(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    circuit = crud_operations.get_circuit(db, skip=skip, limit=limit)
    return circuit


@app.post("/driver/", response_model=schemas.driver)
def create_driver(driver: schemas.driverCreate, db: Session = Depends(get_db)):
    return crud_operations.create_driver(db=db, driver=driver)



#
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
