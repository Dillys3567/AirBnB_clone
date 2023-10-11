#!/usr/bin/python3
"""
    City modules
"""
from models.base_model import BaseModel
from uuid import UUID


class City(BaseModel):
    """
        city class iherit from base
            Atrribute:
                state_id (str)
                name (str)
    """
    state_id = ""
    name = ""

    def _init_(self, *args, **kwargs):
        """
            init
        """
        super()._init_(*args, **kwargs)
