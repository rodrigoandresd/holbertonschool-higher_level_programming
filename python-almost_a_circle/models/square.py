#!/usr/bin/python3

"""square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        public method that assigns an argument to each attribute
        """
        if args is not None and len(args) != 0:
            list_a = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, list_a[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Dictionary representation of a Square
        """
        to_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return to_dict