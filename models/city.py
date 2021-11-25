#!/usr/bin/python3
""" Defines City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Represents City
    Attributes:
        state_id (str): state it belongs to
        name (str): name of the city
    """
    state_id = ""
    name = ""
