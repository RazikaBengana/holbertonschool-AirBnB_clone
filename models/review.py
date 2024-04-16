#!/usr/bin/python3
"""This module defines the 'Review' class that inherits from 'BaseModel'"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The 'Review' class represents a review of a place by a user

    Attributes:
        place_id (str): the ID of the place being reviewed
        user_id (str): the ID of the user who wrote the review
        text (str): the text content of the review
    """

    place_id = ""  # Identifier for the place being reviewed
    user_id = ""  # Identifier for the user who wrote the review
    text = ""  # Text content of the review
