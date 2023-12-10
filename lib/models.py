
# lib/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
