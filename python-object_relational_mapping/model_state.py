""" python file that contains the class definition of a State and
an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State Class
            Attributes:
                __table__(str): Table name of the class
                id(int): The States id, canot be null and is a primary key
                name(str): The States names.
    """
    __table__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(28), nullable=False)
