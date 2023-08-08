#!/usr/bin/python3
#practice.py
"""Define a class BaseModel"""
import uuid
from datetime import datetime

class BaseModel():
    """My base class that deines all common attributes/methods
       for other classes
    """
    def __init__(self, *args, **kwargs):
        """Defines the class object initialisee
        """
        if kwargs:
            if '__class__' in kwargs:
                kwargs.pop('__class__')
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
           the instance

        Returns:
            obj_dict(dict): A dictionary containing all keys and values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict