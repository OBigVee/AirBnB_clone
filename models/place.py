#!/usr/bin/env python3
"""Place class inherit from the BaseModel"""

from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """public class attributes"""

    city_id: str = str()
    user_id: str = str()
    name: str = str()
    description: str = str()
    number_rooms: str = str()
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str]
