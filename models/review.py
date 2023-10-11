#!/usr/bin/python3
"""
    Review modules
"""
from models.base_model import BaseModel
from uuid import UUID


class Review(BaseModel):
    """
        class Review:
            Attribute:
                place_id : id(str)
                user_id : user id(str)
                text : str
    """
    place_id = ""
    user_id = ""
    text = ""

    def _init_(self, *args, **kwargs):
        """
            init
        """
        super()._init_(*args, **kwargs)
