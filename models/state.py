#!/usr/bin/python3
"""
    State modules
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        Class state inherit from Base
            Attribute:
                name (str) : name of state
    """
    name = ""

    def _init_(self, *args, **kwargs):
        """
            Init
        """
        super()._init_(*args, **kwargs)
