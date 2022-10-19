#!/usr/bin/python3

"""
First clase Base
"""


from multiprocessing.sharedctypes import Value
import json


class Base:
    """
    this clase base of this proyect
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []: 
            return "[]"
        return json.dumps(list_dictionaries)
