#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    res = session.query(State).filter(State.name.like(argv[4])).all()

    if res:
        print("{}".format(res[0].id))
    else:
        print("Not Found")
    session.close()