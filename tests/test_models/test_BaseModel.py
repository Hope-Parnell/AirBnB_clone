#!/usr/bin/python3
"""This module tests the BaseModel class"""


import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel Class"""

    # Setting up using ClassMethod to check __init__

    def setUp(self):
        a = BaseModel()
        b = BaseModel()
        c = BaseMode(id=69, created_at="1000-07-29T12:14:07.132263", 
            updated_at="1020-02-13T07:10:03.134263")
        #c = BaseModel()

    def tearDown(self):
        pass

    # Testing correct values happened during __init__

    def testIDUniqueness(self):
        self.assertNotEqual(a.id, b.id)
        #check types
        self.assertEqual(c.id, 69)
        self.assertIsInstance(c.created_at, datetime.datetime)
        self.assertIsInstance(c.updated_at, datetime.datetime)

