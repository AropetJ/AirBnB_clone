#!/usr/bin/python3
# amenity.py

from models.base_model import BaseModel

class Amenity(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
