from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flight'
    seq = Column(Integer, primary_key= True)
    id = Column(Integer)
    name = Column(Text)


class Journey(Base):
    __tablename__ = 'journey'
    seq = Column(Integer,primary_key=True)
    id = Column(Integer)
    flight_id = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    remaining_space = Column(DECIMAL)
    src = Column('from', Integer)
    dest = Column('to', Integer)

class JourneyInventory(Base):
    __tablename__ = 'journey_inventory'
    seq = Column(Integer, primary_key=True)
    id = Column(Integer)
    item_id = Column(Integer)
    quantity = Column(Integer)
    journey_id = Column(Integer)



class Item(Base):
    __tablename__ = 'item'
    seq = Column(Integer, primary_key=True)
    id = Column(Integer)
    name = Column(Text)
    type = Column(Integer)



class Airport(Base):
    __tablename__ = 'airport'
    seq = Column(Integer, primary_key=True)
    id = Column(Integer)
    name = Column(Text)
