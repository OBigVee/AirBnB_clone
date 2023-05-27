#!/usr/bin/env python3
"""Amenity class inherit from the BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Public class attribute"""

    name: str = str()
