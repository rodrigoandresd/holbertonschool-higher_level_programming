#!/usr/bin/python3

"""module that contain the funtion print_square"""


def print_square(size):
    """function that print square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size is float and size < 0:
        raise TypeError("message size must be an integer")

    for i in range(size):
            print(f"#" * size, sep="")
