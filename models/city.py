#!/usr/bin/python3
"""
This module defines the 'City' class which inherits from 'BaseModel';
It represents a city with a unique ID and name, associated with a state
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    The 'City' class encapsulates a city within a state, characterized by
    its 'state_id' (the ID of the state to which the city belongs)
    and 'name' (the city's name) attributes
    """

    state_id = ""  # The ID of the state this city belongs to
    name = ""      # The name of the city
