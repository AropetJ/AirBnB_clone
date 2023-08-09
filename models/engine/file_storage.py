#!/usr/bin/python3
# file_storage.py
"""Defines a class FileStorage"""

import uuid
import pickle
import json
import os
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
                    loaded_objs = pickle.load(file)
                    class_references = {
                        "User": User,
                        "Place": Place,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Review": Review
                    }
                    for key, obj in loaded_objs.items():
                        class_name, obj_id = key.split('.')
                        class_ref = class_references.get(class_name) or User
                        if class_ref:
                            obj_instance = class_ref(**obj)
                            self.__objects[key] = obj_instance
                except pickle.UnpicklingError:
                    pass
