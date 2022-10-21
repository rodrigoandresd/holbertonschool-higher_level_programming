#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
from models.square import Square
import os

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

    def test_Square_creation_3(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_creation(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_Square_representation(self):
        square_repr = str(Square(1, 2, 3, 4))
        result = '[Square] (4) 2/3 - 1'
        self.assertEqual(square_repr, result)

    def test_Square_save_to_file_exists_empty(self):
        Square.save_to_file([])

        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove('Square.json')

    def test_Square_save_to_file_exists(self):
        Square.save_to_file([Square(1)])

        with open('Square.json', 'r') as f:
            self.assertEqual(
                f.read(), '[{"id": 17, "size": 1, "x": 0, "y": 0}]')
        os.remove('Square.json')
