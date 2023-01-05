from sqlalchemy import  Column,  Integer, String, Boolean


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

class circuit(Base):
    __tablename__= "circuit"
    circuit_id = Column(Integer, primary_key=True, index=True)
    circuit_name = Column(String, unique=True, index=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

