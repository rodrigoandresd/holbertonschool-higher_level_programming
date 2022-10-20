#!/usr/bin/python3

"""Unittest for almost a circle project"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class Test_rectangle(unittest.TestCase):
    """Class Test for rectangle models"""

    def test_rectangle_creation_1(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_representation(self):
        rect_r = str(Rectangle(1, 2, 3, 4, 5))
        result = '[Rectangle] (5) 3/4 - 1/2'
        self.assertEqual(rect_r, result)
    
    def test_type(self):
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(TypeError, Rectangle, 10, 8, "3", 5)
        self.assertRaises(TypeError, Rectangle, 10, 8, 3, "5")
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 10, 8, 0, -2)
        self.assertRaises(ValueError, Rectangle, 10, 8, -9, 2)

    def test_area(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_display(self):
        output = io.StringIO()
        sys.stdout = output
        Rectangle(2, 2).display()
        self.assertEqual(output.getvalue(), "##\n##\n")
        output = io.StringIO()
        sys.stdout = output
        Rectangle(2, 2, 1, 1).display()
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")
    
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 89)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)

    def test_inheritance(self):
        r1 = Rectangle(7, 10)
        self.assertEqual(True, isinstance(r1, Base))

    def test_rectangle_to_dictionary_exists(self):
        rect_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        result = {
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4,
            'id': 5
        }
        self.assertEqual(rect_dict, result)

    def test_rectangle_create_exists_1(self):
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89})

    def test_rectangle_create_exists_2(self):
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89, 'width': 1})

    def test_rectangle_create_exists_3(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
