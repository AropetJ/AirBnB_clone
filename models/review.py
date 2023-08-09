#!/usr/bin/python3
# review.py

from models.base_model import BaseModel

class Review(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
