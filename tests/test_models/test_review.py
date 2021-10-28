#!/usr/bin/python3
"""This module tests the Review class"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing the Review Class"""

    def setUp(self):
        """setup before each method"""
        self.a = Review()

    def tearDown(self):
        """cleanup after each method"""
        pass

    # Testing correct values happened during __init__

    def testInstantation(self):
        """test initilization"""
        self.assertEqual(self.a.place_id, "")
        self.assertEqual(self.a.user_id, "")
        self.assertEqual(self.a.text, "")
        aDict = self.a.to_dict()
        b = Review(**aDict)
        self.assertEqual(b.to_dict(), aDict)
        self.assertFalse(self.a is b)
