#!/usr/bin/python3
"""This module tests the Place class"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing the Place Class"""

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
