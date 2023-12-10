# lib/dog.py
from lib.models import Dog, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dogs.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_table(Base):
    Base.metadata.create_all(engine)

def save(name, breed):
    dog = Dog(name=name, breed=breed)
    session.add(dog)
    session.commit()

def all():
    return session.query(Dog).all()

def find_by_name(name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_breed(breed):
    return session.query(Dog).filter_by(breed=breed).all()

def find_by_id(id):
    return session.query(Dog).get(id)

def update_name(id, new_name):
    dog = session.query(Dog).get(id)
    dog.name = new_name
    session.commit()

def update_breed(id, new_breed):
    dog = session.query(Dog).get(id)
    dog.breed = new_breed
    session.commit()

def delete(id):
    dog = session.query(Dog).get(id)
    session.delete(dog)
    session.commit()
