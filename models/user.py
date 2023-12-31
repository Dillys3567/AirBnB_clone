#!/usr/bin/python3
"""
    user modules
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class inherit from base
        Attribute:
            email: (str)
            password: (str)
            first_name: (str)
            last_name: (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def _init_(self, *args, **kwargs):
        """
            Init
        """
        super()._init_(*args, **kwargs)
