#!/usr/bin/env python3
"""User class inherits BaseModel"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage

class User(BaseModel):

    email :str = str()
    password:str = str()
    first_name:str = str()
    last_name:str = str()
