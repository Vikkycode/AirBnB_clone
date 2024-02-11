#!/usr/bin/python3
""" Define a class User """
from models.base_model import BaseModel

class User(BaseModel):
    """Represent a User

    attributes:
    email:(str): email of the user
    password (str): password of the user
    first_name (str): first name of the user
    last_name (str): last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
