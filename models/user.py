#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.
=======


from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import Column

class User(BaseModel):
    """Represent a User.
>>>>>>> 8ca59c908312101d3f374f5b93cd74cac4202b49

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
    """
<<<<<<< HEAD
=======

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """Represents a user in Mysql database.
    Inherits from sqlalchemy Base and links to the Mysql table  users.

    Arttributes:
        __tablesname__ (str): the name of the mysqltable to store users.
        email: (sqlalchemy String): user's email address.
        password (sqlalchemy String): user's password.
        first_name (sqlalchemy String): users' first name.
        last_name (sqlalchemy String): user's last_name.
        places(sqlalchemy relationship): user place relationship.
        reviews (sqlalchemy relationship): user reciew relationship
    """


>>>>>>> 8ca59c908312101d3f374f5b93cd74cac4202b49
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
<<<<<<< HEAD
    places = relationship("Place", backref="user", cascade="delete")
=======
    places = relationship("Review", backref="user", cascade="delete")
>>>>>>> 8ca59c908312101d3f374f5b93cd74cac4202b49
    reviews = relationship("Review", backref="user", cascade="delete")
