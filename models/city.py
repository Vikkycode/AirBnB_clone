#!/usr/bin/python3
""" Define a class City """
from models.base_model import BaseModel

class City(BaseModel):
    """Represent a City

    attributes:
    state_id(str): state id of the city
    name (str): name of the city
    """

    state_id = ""
    name = ""
