#!/usr/bin/python3
"""Define Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Reprsent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): User id.
        text (str): Review message
    """

    place_id = ""
    user_id = ""
    text = ""
