#!/usr/bin/python3
"""
    Amenity modules
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        class Amenity inherit from base
        Attribute:
            name (str)
    """
    name = ""

    def _init_(self, *args, **kwargs):
        """
            str
        """
        super()._init_(*args, **kwargs)
