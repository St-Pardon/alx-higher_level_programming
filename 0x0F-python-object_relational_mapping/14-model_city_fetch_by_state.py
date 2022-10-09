#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session, relationship
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.cities = relationship('City', back_populates='state')
    session = Session(engine)
    res = session.query(City).order_by(City.id.asc()).all()

    for row in res:
        print('{}: ({}) {}'.format(row.state.name, row.id, row.name))
