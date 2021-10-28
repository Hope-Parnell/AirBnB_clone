#!/usr/bin/python3
"""Test the console module"""
import unittest
import console


class TestConsole(unittest.TestCase):
    """Tests the Console"""
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
