#!/usr/bin/python3
"""Define City class."""
form model.base_model import BaseModel

class City(BaseModel):
    """Represent a city.
    Attriutes:
        state_id (str): state id
        name (str):  name of city
    """
    state_id = ""
    name = ""
