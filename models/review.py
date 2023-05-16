#!/usr/bin/env python3
"""Review class inherit from the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attribute"""

    place_id: str = str()  # Place.id
    user_id: str = str()  # User.id
    text: str = str()
