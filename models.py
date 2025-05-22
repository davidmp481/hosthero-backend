
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer)
    cleaner_id = Column(String)
    date = Column(Date)
    checklist = Column(String)

class InventoryItem(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer)
    name = Column(String)
    quantity = Column(Integer)
    threshold = Column(Integer)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer)
    guest_name = Column(String)
    checkin = Column(Date)
    checkout = Column(Date)
