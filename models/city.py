#!/usr/bin/env python3
"""City class inherit from the BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """public class attributes"""

    state_id: str = str()
    name: str = str()
