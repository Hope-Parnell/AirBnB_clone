#!/usr/bin/python3
"""This module tests the User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing the User Class"""

    def setUp(self):
        """setup before each method"""
        self.a = User()

    def tearDown(self):
        """cleanup after each method"""
        pass

    # Testing correct values happened during __init__

    def testInstantation(self):
        """test initilization"""
        self.assertEqual(self.a.email, "")
        self.assertEqual(self.a.password, "")
        self.assertEqual(self.a.first_name, "")
        self.assertEqual(self.a.last_name, "")
        aDict = self.a.to_dict()
        b = User(**aDict)
        self.assertEqual(b.to_dict(), aDict)
        self.assertFalse(self.a is b)
