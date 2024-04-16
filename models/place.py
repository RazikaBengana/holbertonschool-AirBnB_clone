#!/usr/bin/python3
"""This module defines the 'Place' class that inherits from 'BaseModel'"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    The 'Place' class represents a Place for Airbnb clone

    Attributes:
        - city_id (str): the city ID where the place is located
        - user_id (str): the user ID of the place's owner
        - name (str): the name of the place
        - description (str): a description of the place
        - number_rooms (int): the number of rooms in the place
        - number_bathrooms (int): the number of bathrooms in the place
        - max_guest (int): the maximum number of guests the place can accommodate
        - price_by_night (int): the price for staying one night
        - latitude (float): the latitude of the place's location
        - longitude (float): the longitude of the place's location
        - amenity_ids (list): a list of amenity IDs available at the place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
