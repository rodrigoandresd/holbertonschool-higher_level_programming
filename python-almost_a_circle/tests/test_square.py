#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
from models.square import Square


class Test_square(unittest.TestCase):
    """Class Test for square models"""

    def test_square_creation_1(self):
        rect = Square(1, 2)
        self.assertEqual(rect.size, 1)
        self.assertEqual(rect.x, 2)

    def test_type_value(self):
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, 2.5)
        self.assertRaises(TypeError, Square, [2, 5])
        self.assertRaises(TypeError, Square, (2, 5))
        self.assertRaises(TypeError, Square, 10, 8, "3")
        self.assertRaises(TypeError, Square, 10, 3.5, 3)
        self.assertRaises(TypeError, Square)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -10)
        self.assertRaises(ValueError, Square, 10, -3, 0)
        self.assertRaises(ValueError, Square, 10, 3, -10)

    def test_Square_creation(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)
