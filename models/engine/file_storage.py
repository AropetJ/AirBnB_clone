#!/usr/bin/python3
# file_storage.py
"""Defines a class FileStorage"""

import uuid
import pickle
import json
import os
from models.user import User

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
        with open(self.__file_path, "wb") as file:
            pickle.dump(self.__objects, file)

    def reload(self):
        """_summary_
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "rb") as file:
                try:
                    loaded_objs = pickle.load(file)
                    for key, obj in loaded_objs.items():
                        self.__objects[key] = obj
                except pickle.UnpicklingError:
                    pass
