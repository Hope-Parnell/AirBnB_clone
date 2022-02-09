#!/usr/bin/python3
"""This module tests the Place class"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing the Place Class"""
    def setUp(self):
        """setup before each method"""
        self.a = Place()
        pass

    def tearDown(self):
        """cleanup after each method"""
        pass

    # Testing correct values happened during __init__

    def testInstantation(self):
        """tests initilization"""
        self.assertEqual(self.a.city_id, "")
        self.assertEqual(self.a.user_id, "")
        self.assertEqual(self.a.name, "")
        self.assertEqual(self.a.description, "")
        self.assertEqual(self.a.number_rooms, 0)
        self.assertEqual(self.a.number_bathrooms, 0)
        self.assertEqual(self.a.max_guest, 0)
        self.assertEqual(self.a.price_by_night, 0)
        self.assertEqual(self.a.latitude, 0.0)
        self.assertEqual(self.a.longitude, 0.0)
        self.assertEqual(self.a.amenity_ids, [])
        aDict = self.a.to_dict()
        b = Place(**aDict)
        self.assertEqual(b.to_dict(), aDict)
        self.assertFalse(self.a is b)
