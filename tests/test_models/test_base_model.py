#!/usr/bin/python3
"""This module tests the BaseModel class"""


import unittest
from models.base_model import BaseModel
import datetime
import json


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel Class"""

    # Setting up using ClassMethod to check __init__

    def setUp(self):
        self.a = BaseModel()
        self.b = BaseModel()
        self.c = BaseModel(id=69, created_at="1000-07-29T12:14:07.132263",
                           updated_at="1020-02-13T07:10:03.134263",
                           __class__="test123")

    def tearDown(self):
        pass

    # Testing correct values happened during __init__

    def testIDs(self):
        self.assertIsInstance(self.a.id, str, "BaseModel ID is not a string")
        self.assertNotEqual(self.a.id, self.b.id,
                            "BaseModel IDs are not unique")
        self.assertEqual(self.c.id, 69,
                         "BaseModel init does not assign ID (check ID type)")

    def testDates(self):
        self.assertIsInstance(self.c.created_at, datetime.datetime,
                              "BaseModel's created_at isn't a datetime object")
        self.assertIsInstance(self.c.updated_at, datetime.datetime,
                              "BaseModel's updated_at isn't a datetime object")

    def teststr(self):
        s = ["[BaseModel] (69) {'id': 69, ",
             "'created_at': datetime.datetime",
             "(1000, 7, 29, 12, 14, 7, 132263), ",
             "'updated_at': datetime.datetime",
             "(1020, 2, 13, 7, 10, 3, 134263)}"]
        stringline = s[0] + s[1] + s[2] + s[3] + s[4]
        self.assertEqual(str(self.c), stringline, "str(BaseModel) error")

    def testSave(self):
        # check if updated_at changed
        lastUpdate = str(self.c.updated_at)
        self.c.save()
        self.assertNotEqual(str(self.c.updated_at),
                            lastUpdate,
                            "updated_at did not change when using save()")
        # make sure file.json updated
        with open("file.json") as f:
            txt = f.read()
            self.assertTrue(json.dumps(self.c.to_dict()) in txt,
                            ".json not updated when using save()")

    def testToDict(self):
        # created_at and updated_at are ISO strings
        cDict = self.c.to_dict()
        s = ["{'id': 69, 'created_at': ",
             "'1000-07-29T12:14:07.132263', ",
             "'updated_at': '1020-02-13T07:10:03.134263',",
             " '__class__': 'BaseModel'}"]
        stringline = s[0] + s[1] + s[2] + s[3]
        self.assertEqual(str(cDict), stringline, "dict not match in toDict()")
        self.assertIsInstance(cDict["updated_at"], str,
                              "updated_at not ISO string. used in toDict()")
        self.assertIsInstance(cDict["created_at"], str,
                              "created_at not ISO string. used in toDict()")

    def testpassClass(self):
        self.assertEqual(self.c.__class__, BaseModel,
                         "class is assigned as attribute in __init__")
