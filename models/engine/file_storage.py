#!/usr/bin/python3
# file_storage.py
"""Defines a class FileStorage"""
import json
import os

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (object): The object whose key is to be set
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file.
        """
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    loaded_objs = json.load(file)
                    for key, obj_dict in loaded_objs.items():
                        class_name, obj_id = key.split('.')
                        class_ref = globals().get(class_name)
                        if class_ref:
                            obj_instance = class_ref(**obj_dict)
                            self.__objects[key] = obj_instance
                except json.JSONDecodeError:
                    pass
