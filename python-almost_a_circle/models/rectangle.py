#!/usr/bin/python3

"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle subclass from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """inicilizes variables and methods"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validator method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Method that returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """
        public method that prints in stdout the Rectangle with the character #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
        public method that assigns an argument to each attribute
        """
        if args is not None and len(args) != 0:
            list_a = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, list_a[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Dictionary representation of a Rectangle
        """
        to_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return to_dict
