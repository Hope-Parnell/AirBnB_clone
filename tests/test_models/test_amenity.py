#!/usr/bin/python3
"""This module tests the Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing the Amenity Class"""

    # Setting up using ClassMethod to check __init__

    def setUp(self):
        """setup before each method"""
        self.a = Amenity()
        self.b = Amenity()
        pass

    def tearDown(self):
        """cleanup after each method"""
        pass

    # Testing correct values happened during __init__

    def testInstantation(self):
        """tests initilization"""
        self.assertNotEqual(self.a.id, self.b.id)
        self.assertEqual(self.a.name, "")
        aDict = self.a.to_dict()
        b = Amenity(**aDict)
        self.assertEqual(b.to_dict(), aDict)
        self.assertFalse(self.a is b)
