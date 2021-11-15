#!/usr/bin/python3
""" Defines Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Represents Review
    Attributes:
        place_id (str): place reviewed
        user_id (str): review made by
        text (str): review
    """

    place_id = ""
    user_id = ""
    text = ""
