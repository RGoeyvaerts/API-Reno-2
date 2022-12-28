from pydantic import BaseModel


class driverBase(BaseModel):
    driver_name: str
    description: str | None = None


class driverCreate(driverBase):
    pass


class driver(driverBase):
    driver_id: int
    race_number: int
    country: str

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