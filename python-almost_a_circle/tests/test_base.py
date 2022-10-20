#!/usr/bin/python3

"""tests for almost a circle project"""

import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_exists(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])
    
    def test_to_json_string(self):
        output = io.StringIO()
        sys.stdout = output
        json_dictionary = Base.to_json_string(None)
        print(json_dictionary)
        self.assertEqual(output.getvalue(), "[]\n")
        dic1 = {"x": 10, "width": 5, "id": 2, "height": 9, "y": 0}
        dic2 = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        my_string = Base.to_json_string([dic1, dic2])
        dictionary = Base.from_json_string(my_string)
        self.assertEqual(dictionary, [dic1, dic2])
        s1 = {"x": 10, "size": 4, "id": 2, "y": 0}
        s2 = {"x": 2, "size": 10, "id": 1, "y": 8}
        my_string = Base.to_json_string([s1, s2])
        dictionary = Base.from_json_string(my_string)
        self.assertEqual(dictionary, [s1, s2])

    def test_save_to_file(self):
        output = io.StringIO()
        sys.stdout = output
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            print(file.read())
        self.assertEqual(output.getvalue(), "[]\n")
        output = io.StringIO()
        sys.stdout = output
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            print(file.read())
        self.assertEqual(output.getvalue(), "[]\n")
        r1 = {"x": 10, "width": 5, "id": 2, "height": 9, "y": 0}
        r2 = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}

    def test_from_json_string(self):
        output = io.StringIO()
        sys.stdout = output
        list_output = Rectangle.from_json_string(None)
        print("[{}] {}".format(type(list_output), list_output))
        self.assertEqual(output.getvalue(), "[<class 'list'>] []\n")
        output = io.StringIO()
        sys.stdout = output
        list_output = Square.from_json_string(None)
        print("[{}] {}".format(type(list_output), list_output))
        self.assertEqual(output.getvalue(), "[<class 'list'>] []\n")

    def test_create(self):
        output = io.StringIO()
        sys.stdout = output
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r2)
        self.assertEqual(output.getvalue(), "[Rectangle] (3) 1/0 - 3/5\n")
        self.assertFalse(r1 is r2)
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)

    def test_load_from_file(self):
        output = io.StringIO()
        sys.stdout = output
        list_rectangles_output = Rectangle.load_from_file()
        print(list_rectangles_output)
        self.assertEqual(output.getvalue(), "[]\n")
        input = [Rectangle(4, 5), Rectangle(2, 3)]
        Rectangle.save_to_file(input)
        output = Rectangle.load_from_file()
        i = 0
        for item in output:
            self.assertEqual(str(item), str(input[i]))
            i += 1
        input = [Square(4), Square(2)]
        Square.save_to_file(input)
        output = Square.load_from_file()
        i = 0
        for item in output:
            self.assertEqual(str(item), str(input[i]))
            i += 1

if __name__ == '__main__':
    unittest.main()