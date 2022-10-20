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
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 10, 8, 0, -2)
        self.assertRaises(ValueError, Rectangle, 10, 8, -9, 2)

    def test_area(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_class_method_presence(self):
        """Test that the Rectangle methods are all present"""
        l1 = dir(Rectangle)
        self.assertIn('__init__', l1)
        self.assertIn('width', l1)
        self.assertIn('height', l1)
        self.assertIn('x', l1)
        self.assertIn('y', l1)
        self.assertIn('area', l1)
        self.assertIn('display', l1)
        self.assertIn('__str__', l1)
        self.assertIn('update', l1)
        self.assertIn('to_dictionary', l1)
        self.assertIn('from_json_string', l1)
        self.assertIn('load_from_file', l1)
