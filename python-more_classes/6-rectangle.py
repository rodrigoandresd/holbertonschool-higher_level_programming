#!/usr/bin/python3

"""class rectangle that defines a Rectangle empty"""


class Rectangle:
    """Rectangle class definition"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """__init__ method: a rectangle object.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        new_str = ""
        if self.__height == 0 or self.__width == 0:
            return new_str
        for i in range(self.__height):
            new_str += '#' * self.__width
            if i != self.height - 1:
                new_str += '\n'
        return new_str

    def __repr__(self):
        """__repr__ Method returns the internal representation of an object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
