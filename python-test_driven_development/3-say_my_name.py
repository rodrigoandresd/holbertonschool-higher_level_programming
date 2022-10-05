#!/usr/bin/python3

"""
module that contain the function say_my_name
"""

def say_my_name(first_name, last_name=""):
    if type(first_name) not in [str]:
                raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
                raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
