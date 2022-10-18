#!/usr/bin/python3

"""
First clase Base
"""


from multiprocessing.sharedctypes import Value


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
