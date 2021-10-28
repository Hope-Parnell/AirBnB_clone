#!/usr/bin/python3
"""This module tests the BaseModel class"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel Class"""

    # Setting up using ClassMethod to check __init__

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # Testing correct values happened during __init__

    def testInstantation(self):
        pass

    # Testing instantation errors

    def testInitErrors(self):
        with self.assertRaises(TypeError):
            pass
