#!/usr/bin/python3
# city.py

from models.base_model import BaseModel

class City(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
