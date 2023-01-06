from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import os
import crud_operations
import models
import schemas
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth
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



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )

    return {"access_token": access_token, "token_type": "bearer"}







@app.get("/drivers/", response_model=list[schemas.driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = crud_operations.get_all_drivers(db, skip=skip, limit=limit)
    return drivers

@app.post("/driver/", response_model=schemas.driver)
def create_driver(driver: schemas.driverCreate, db: Session = Depends(get_db)):
    db_driver = crud_operations.get_driver_by_name(db, driver_name=driver.driver_name)
    if db_driver:
        raise HTTPException(status_code=400, detail="Driver already registered")
    return crud_operations.create_driver(db=db, driver=driver)


@app.put("/drivers/{driver_id}")
def update_racenumber(driver_id: int, race_number: str):
    session = Session(bind=engine, expire_on_commit=False)
    racenumber = session.query(models.driver).get(driver_id)
    if racenumber:
        racenumber.race_number = race_number
        session.commit()
    session.close()
    if not racenumber:
        raise HTTPException(status_code=404, detail=f"driver with id {driver_id} not found")

    return racenumber

@app.delete("/driver/{driver_id}")
def delete_driver(driver_id: int):
    with Session(engine) as session:
        driver = session.get(models.driver, driver_id)
        if not driver:
            raise HTTPException(status_code=404, detail="driver not found")
        session.delete(driver)
        session.commit()
        return {"ok": True}








@app.get("/teams/", response_model=list[schemas.team])
def get_all_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = crud_operations.get_all_teams(db, skip=skip, limit=limit)
    return teams

@app.post("/team/", response_model=schemas.team)
def create_team(team: schemas.teamCreate, db: Session = Depends(get_db)):
    db_team = crud_operations.get_team_by_name(db, team_name=team.team_name)
    if db_team:
        raise HTTPException(status_code=400, detail="Team already registered")
    return crud_operations.create_team(db=db, team=team)



@app.delete("/team/{team_id}")
def delete_team(team_id: int):
    with Session(engine) as session:
        team = session.get(models.team, team_id)
        if not team:
            raise HTTPException(status_code=404, detail="team not found")
        session.delete(team)
        session.commit()
        return {"ok": True}








@app.get("/circuits/", response_model=list[schemas.circuit])
def read_circuit(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    circuit = crud_operations.get_circuit(db, skip=skip, limit=limit)
    return circuit


@app.post("/circuit/", response_model=schemas.circuit)
def create_circuit(circuit: schemas.circuitCreate, db: Session = Depends(get_db)):
    db_circuit = crud_operations.get_circuit_by_name(db, circuit_name=circuit.circuit_name)
    if db_circuit:
        raise HTTPException(status_code=400, detail="Circuit already registered")
    return crud_operations.create_circuit(db=db, circuit=circuit)

@app.delete("/circuits/{circuit_id}")
def delete_circuit(circuit_id: int):
    with Session(engine) as session:
        circuit = session.get(models.circuit, circuit_id)
        if not circuit:
            raise HTTPException(status_code=404, detail="circuit not found")
        session.delete(circuit)
        session.commit()
        return {"ok": True}




@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud_operations.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_operations.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_operations.create_user(db=db, user=user)