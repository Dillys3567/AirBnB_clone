#!/usr/bin/python3
"""Define Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place.
    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): Name of place.
        description (str): Description of the place.
        number_rooms (int): Number of rooms.
        number_bathrooms (int): Number of bathrooms.
        max_guest (int): Maximum number of guests.
        price_by night (int): Price per night.
        latitude (float): Latitude.
        longitude (float): Longitude.
        amenity_ids (list): List of amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
