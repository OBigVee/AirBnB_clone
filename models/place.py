#!/usr/bin/python3
""" Defines Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Represents Place
    Attributes:
        city_id (str): city of location
        user_id (str): owner
        name (str): name of place
        description (str): short desc about place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guests (int): number of guests we are able to host
        price_by_night (int): price of one night
        latitude (float): latitude part of location
        longitude (float): longitude part of location
        amenity_id (str): amenity it belongs to
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
    amenity_id = ""
