#!/usr/bin/python3
"""
This module defines the 'User' class which inherits from 'BaseModel';
It is used to represent a user in a system, with attributes for email, password, first name, and last name;
This setup allows for the creation, manipulation, and storage of user information in a structured manner
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The 'User' class inherits from 'BaseModel' and includes properties for user details;
    Each User instance will have an email, password, first name, and last name, all
    initialized as empty strings but can be set to represent a user in the system
    """

    email = ""  # Email address of the user
    password = ""  # Password for user authentication
    first_name = ""  # User's first name
    last_name = ""  # User's last name
