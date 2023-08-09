#!/usr/bin/python3
# user.py
"""Defines a class User that inherits from BaseModel"""

from models.base_model import BaseModel
class User(BaseModel):
    """
    A class User that inherits from BaseModel class
    Args:
        BaseModel (class): The class to inherit from
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
