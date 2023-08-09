#!/usr/bin/python3
# state.py

from models.base_model import BaseModel

class State(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
