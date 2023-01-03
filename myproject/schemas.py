from pydantic import BaseModel


class driverBase(BaseModel):
    driver_name: str


class driverCreate(driverBase):
    race_number: int
    country: str



class driver(driverBase):
    driver_id: int


    class Config:
        orm_mode = True


class teamBase(BaseModel):
    team_name: str


class teamCreate(teamBase):
    pass


class team(teamBase):
    team_id: int

    class Config:
        orm_mode = True

class circuitBase(BaseModel):
    circuit_name: str

class circuitCreate(circuitBase):
    pass

class circuit(circuitBase):
    circuit_id: int

    class Config:
        orm_mode = True
