#!/usr/bin/python3

"""class rectangle that defines a Rectangle empty"""


class Rectangle:
    """Rectangle class definition"""
    def __init__(self, width=0, height=0):
        """__init__ method: a rectangle object.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """define area method, evaluate rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """define perimeter method, evaluate rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.height + self.width)
