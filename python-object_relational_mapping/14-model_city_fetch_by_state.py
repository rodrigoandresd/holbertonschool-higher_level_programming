#!/usr/bin/python3
"""script that changes the name of a State object from the
database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

if __name__ == "__main__":
    a1 = sys.argv[1]
    a2 = sys.argv[2]
    a3 = sys.argv[3]
    en = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(a1, a2, a3),
                       pool_pre_ping=True)
    en.connect()
    metadata = MetaData()
    session = Session(en)
    for state_instance, city_instance in session.query(State, City).filter(
            State.id == City.state_id).all():
        print("{}: ({}) {}".format(state_instance.name,
                                   city_instance.id, city_instance.name))
    session.close()
