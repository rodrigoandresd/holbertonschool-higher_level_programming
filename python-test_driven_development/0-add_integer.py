#!/usr/bin/python3

"""
module that adds 2 integers
"""


def add_integer(a, b=98):
    """addition function

    Args:
        a: first integer or float
        b: second  or float 
    Returns:
        The return value. a + b
    """
    if not a or not isinstance (a, (float, int)):
        raise TypeError("a must be an integer")
    if not b or not isinstance (b, (float, int)):
        raise TypeError("b must be an integer")
    
    return (int(a) + int(b))
