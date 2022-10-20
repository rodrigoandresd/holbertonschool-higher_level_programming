#!/usr/bin/python3

"""tests for almost a circle project"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class test"""
    def test_auto_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
    def test_auto_id_plus_one(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)
    def test_auto_id_saved(self):
        b2 = Base(89)
        self.assertEqual(b2.id, 89)
    def test_to_json_str_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')
    def test_to_json_str_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')
    def test_to_json_str_id(self):
        self.assertEqual(Base.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
    def test_to_json_str_id_exist(self):
        self.assertEqual(Base.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
if __name__ == '__main__':
    unittest.main()