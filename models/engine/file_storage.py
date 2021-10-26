#!/usr/bin/python3
"""TEEETH"""
import json
import sys
from models.base_model import BaseModel



class FileStorage:
    """FSFSFSFS"""  
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dict"""
        return self.__objects
    
    def new(self, obj):
        """updates dict with new obj"""
        self.__objects.update({type(obj).__name__ + "." + str(obj.id): obj})
    
    def save(self):
        "saves json to file"
        newDict = dict(self.all())
        for o in newDict:
            newDict.update({o: newDict[o].to_dict()})
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(newDict))  

    def reload(self):
        "returns object from json file"
        try:
            with open(self.__file_path, 'r') as f:
                newDict = json.loads(f.read())
                for o in newDict:
                    objDict = newDict.get(o)
                    #newObj is a string of class name
                    #newObj = objDict.get("__class__")
                    #change BaseModel to actual class type
                    newDict.update({o: BaseModel(**objDict)})
                    print(newDict)
                self.__objects = newDict
        except Exception:
            pass
    



    
    