#!/usr/bin/python3
"""Base model class"""
from . import storage
import json
import uuid
import datetime


class BaseModel():
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initialize a new Base"""
        """ self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
 """
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_obj = datetime.datetime.strptime
                    (value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date_obj)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()  # to be updated
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        to_dict = {}
        to_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                to_dict[key] = value.isoformat()
            else:
                to_dict[key] = value

        return to_dict
        """   self.created_at = datetime.datetime.utcnow().isoformat()
        self.updated_at = datetime.datetime.utcnow().isoformat()
        return self.__dict__ """

    def __str__(self):
        """Return the print() and str() representation of the BaseModel"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)


# Tests goes here
