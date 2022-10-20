#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """Class Test for rectangle models"""

    def test_rectangle_creation_1(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
    
    def test_type(self):
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(TypeError, Rectangle, 10, 8, "3", 5)
        self.assertRaises(TypeError, Rectangle, 10, 8, 3, "5")

    def tes_value(self):
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
