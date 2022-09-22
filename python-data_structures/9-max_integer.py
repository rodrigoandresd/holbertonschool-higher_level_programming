#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    new_list = sorted(my_list)
    return new_list[-1]
