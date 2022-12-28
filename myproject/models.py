from sqlalchemy import  Column,  Integer, String


from database import Base


class driver(Base):
    __tablename__ = "driver"

    driver_id = Column(Integer, primary_key=True, index=True)
    driver_name = Column(String, unique=True, index=True)
    race_number = Column(Integer, unique=True, index=True)
    country = Column(String, index=True)



class team(Base):
    __tablename__ = "team"

    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String,unique=True, index=True)


