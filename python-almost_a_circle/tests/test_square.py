#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
from models.square import Square


class Test_square(unittest.TestCase):
    """Class Test for square models"""

    def test_type_value(self):
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, 2.5)
        self.assertRaises(TypeError, Square, [2, 5])
        self.assertRaises(TypeError, Square, (2, 5))
        self.assertRaises(TypeError, Square, 10, 8, "3")
        self.assertRaises(TypeError, Square, 10, 3.5, 3)
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 5, 6)
        self.assertRaises(TypeError, Square)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -10)
        self.assertRaises(ValueError, Square, 10, -3, 0)
        self.assertRaises(ValueError, Square, 10, 3, -10)
