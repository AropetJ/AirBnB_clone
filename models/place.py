#!/usr/bin/python3
# place.py

from models.base_model import BaseModel

class Place(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
