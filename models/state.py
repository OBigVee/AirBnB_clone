#!/usr/bin/python3
""" Defines state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Represents State objects in our application
    Attributes:
        name (str): name of state
    """

    name = ""
