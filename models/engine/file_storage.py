#!/usr/bin/python3
"""Contains class for file storage and loading"""
import json
import sys
from models.base_model import BaseModel
from models.user import User
import models


class FileStorage:
    """Class for saving an loading objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dict of all current objects"""
        return self.__objects

    def new(self, obj):
        """updates dict with new obj"""
        self.__objects.update({type(obj).__name__ + "." + str(obj.id): obj})

    def save(self):
        "saves all objects to json file"
        newDict = dict(self.all())
        for o in newDict:
            newDict.update({o: newDict[o].to_dict()})
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(newDict))

    def reload(self):
        "loads all objects from json file"
        try:
            with open(self.__file_path, 'r') as f:
                newDict = json.loads(f.read())
                for o in newDict:
                    objDict = newDict.get(o)
                    newObj = objDict.get("__class__")
                    objClass = models.dict_greyson.get(newObj)
                    newDict.update({o: objClass(**objDict)})
                self.__objects = newDict
        except Exception:
            pass
