#!/usr/bin/python3

"""
    Module for geometry class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer_validator method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """__init__ constructor method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
