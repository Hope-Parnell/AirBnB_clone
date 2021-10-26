#!/usr/bin/python3
"""Module contains the BaseModel class"""
import datetime
from uuid import uuid4



class BaseModel:
    """Defines BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initilizes the object"""
        if len(kwargs) > 0:
            for item in kwargs:
                if item == 'created_at' or item == 'updated_at':
                    self.__dict__.update({item: datetime.datetime.strptime(kwargs.get(item), '%Y-%m-%dT%H:%M:%S.%f')})
                else:
                    self.__dict__.update({item: kwargs.get(item)})
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        newDict = dict(self.__dict__)
        newDict.update({"__class__": type(self).__name__})
        newDict.update({"updated_at": self.updated_at.isoformat()})
        newDict.update({"created_at": self.created_at.isoformat()})
        return newDict


