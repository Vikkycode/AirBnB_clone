#!/usr/bin/python3
""" Define a class User """
from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a Place

    attributes:
    city_id:(str): city id of the place
    user_id (str): user_id of the place
    name (str): name of the place
    description (str): description of the place
    number_room (int): The number of rooms of the place
    number_bathroom (int): The number of bathrooms of the place
    max_guest (int): The maximum number of guests of the place.
    price_by_night (int): The price by night of the place.
    latitude (float): The latitude of the place.
    longitude (float): The longitude of the place.
    amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = 0
    number_bathroom = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
