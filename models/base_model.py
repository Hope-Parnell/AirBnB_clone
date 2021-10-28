#!/usr/bin/python3
"""Module contains the BaseModel class"""
import datetime
from uuid import uuid4
import models


class BaseModel:
    """Defines BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initilizes the object"""
        if len(kwargs) > 0:
            for item in kwargs:
                if item == 'created_at' or item == 'updated_at':
                    self.__dict__.update({item: datetime.datetime.strptime(
                        kwargs.get(item), '%Y-%m-%dT%H:%M:%S.%f')})
                elif item == "__class__":
                    pass
                else:
                    self.__dict__.update({item: kwargs.get(item)})
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self):
        """string representation for the object"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """saves the object to file"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates a dictionary for the object"""
        newDict = dict(self.__dict__)
        newDict.update({"__class__": type(self).__name__})
        newDict.update({"updated_at": self.updated_at.isoformat()})
        newDict.update({"created_at": self.created_at.isoformat()})
        return newDict
