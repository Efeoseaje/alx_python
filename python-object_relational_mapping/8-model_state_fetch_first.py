"""
script that lists the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    """ Connect to the database """
    Database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(Database_url)

    """" Define a Session class"""
    Session = sessionmaker(bind=engine)

    """ Instantiate a session"""
    session = Session()

    instance = session.query(State).first()

    if instance is None:
        print("Nothing")

    else:
        print("{}: {}".format(instance.id, instance.name))
