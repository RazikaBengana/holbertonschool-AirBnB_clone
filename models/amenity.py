#!/usr/bin/python3
"""
This module defines the 'Amenity' class which inherits from 'BaseModel';
The 'Amenity' class represents amenities available in a property, such as a pool or free WiFi for example
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The 'User' class defines attributes and methods for Amenity instances;
    Currently, it only has one attribute:
    - name: name of the amenity
    """

    name = ""
