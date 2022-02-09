#!/usr/bin/python3
"""This module tests the State class"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Testing the State Class"""

    def setUp(self):
        """setup before each method"""
        self.a = State()

    def tearDown(self):
        """cleanup after each method"""
        pass

    # Testing correct values happened during __init__

    def testInstantation(self):
        """test initilization"""
        self.assertEqual(self.a.name, "")
        aDict = self.a.to_dict()
        b = State(**aDict)
        self.assertEqual(b.to_dict(), aDict)
        self.assertFalse(self.a is b)
