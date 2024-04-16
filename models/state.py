#!/usr/bin/python3
"""
This is a module that defines the 'State' class which inherits from 'BaseModel'
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    The 'State' class represents entities that handle either geographical or logical states;
    It has an attribute 'name' that stores the name of the state
    """

    name = ""  # A string attribute to store the name of the state
