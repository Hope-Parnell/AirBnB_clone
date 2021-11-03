#!/usr/bin/python3
"""Module contains the BaseModel class"""
import datetime
from uuid import uuid4
import models


class BaseModel:
    """Defines BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initilizes the object"""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        for key in kwargs:
            if key == "__class__":
                continue
            item = kwargs[key]
            oType = type(self)
            if key in self.__dict__:
                iType = type(self.__dict__[key])
                if iType is datetime.datetime:
                    item = datetime.datetime.strptime(
                        item, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    try:
                        item = iType(item)
                    except Exception:
                        pass
            elif key in oType.__dict__:
                iType = type(oType.__dict__[key])
                if iType is datetime.datetime:
                    item = datetime.datetime.strptime(
                        item, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    try:
                        item = iType(item)
                    except Exception:
                        pass
            self.__dict__.update({key: item})

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
