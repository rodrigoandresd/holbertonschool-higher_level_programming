#!/usr/bin/python3
"""Function that returns the Pascal's triangle"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal's triangle of n"""

    list_pt = []

    if n <= 0:
        return list_pt

    if n == 1:
        list_pt = [[1]]
        return list_pt

    list_pt = [[1], [1, 1]]

    for prev_val in range(1, n - 1):

        line = [1]

        for nxt_val in range(0, len(list_pt[prev_val]) - 1):

            line.extend([list_pt[prev_val][nxt_val] + list_pt[prev_val][nxt_val + 1]])

        line += [1]
        list_pt.append(line)

    return list_pt
