#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class test for max_integer"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_max_uniq(self):
        self.assertEqual(max_integer([3]), 3)
    def test_max_lesso(self):
        self.assertEqual(max_integer([13, -8, 0, 1]), 13)
    def test_max_negative(self):
        self.assertEqual(max_integer([-10, -8, -2, -4]), -2)
    def test_max_none(self):
        self.assertEqual(max_integer([]), None)