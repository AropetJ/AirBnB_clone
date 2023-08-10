#!/usr/bin/python3
# file_storage.py
"""Defines a class FileStorage"""

import uuid
import pickle
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Class to store data in files."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the objects stored on this storage
        """
        return self.__objects

    def new(self, obj):
        """
        Adds an object to be saved

        Args:
            obj (object): 
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file
        """
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "wb") as file:
            pickle.dump(serialized_objs, file)

    def reload(self):
        """_summary_
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "rb") as file:
                try:
                    self.__objects = pickle.load(file)
                except pickle.UnpicklingError:
                    pass
                except pickle.UnpicklingError:
                    pass
