#!/usr/bin/python3

"""
module that contain the function matrix_divided
"""


def matrix_divided(matrix, div):
    """
     that divides all elements of a matrix
    """
    le = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
            raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if not matrix or not matrix[0]:
        raise TypeError(e)

    if type(matrix) is not list:
        raise TypeError(e)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(le)

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not element or not isinstance(element, (float, int)):
                raise TypeError(le)

    return list(map(lambda row: list(map(lambda num:
                                         round(num / div, 2), row)), matrix))
