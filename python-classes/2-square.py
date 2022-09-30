#!/usr/bin/python3

""" Square class definition"""


class Square:
    """ Square class definition"""

    def __init__(self, size=0):
        """__init__ method: a square object.
        args: size - size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
