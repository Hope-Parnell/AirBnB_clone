#!/usr/bin/python3
"""This module tests the City class"""


import unittest
from models.city import City


class TestAmenity(unittest.TestCase):
    """Testing the City Class"""

    # Setting up using ClassMethod to check __init__

    def setUp(self):
        """setup before each method"""
        self.a = City()

    def tearDown(self):
        """cleanup after each method"""
        pass

    # Testing correct values happened during __init__

    def testInstantation(self):
        """test initilization"""
        self.assertEqual(self.a.name, "")
        self.assertEqual(self.a.state_id, "")
        aDict = self.a.to_dict()
        b = City(**aDict)
        self.assertEqual(b.to_dict(), aDict)
        self.assertFalse(self.a is b)
