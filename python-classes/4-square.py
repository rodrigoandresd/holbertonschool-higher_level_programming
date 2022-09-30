#!/usr/bin/python3

""" Square class definition"""


class Square:
    """ Square class definition"""

    def __init__(self, size=0):
        """__init__ method: a square object.
        args: size - size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size
        
    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
            
        self.__size = value

    def area(self):
        """define area method, evaluate square area"""
        return self.__size ** 2
