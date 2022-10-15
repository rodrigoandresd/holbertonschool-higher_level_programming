#!/usr/bin/python3
"""Function that returns the Pascal's triangle"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal's triangle of n"""

    lt = []

    if n <= 0:
        return lt

    if n == 1:
        lt = [[1]]
        return lt

    lt = [[1], [1, 1]]

    for prev_val in range(1, n - 1):

        line = [1]

        for nxt_val in range(0, len(lt[prev_val]) - 1):

            line.extend([lt[prev_val][nxt_val] + lt[prev_val][nxt_val + 1]])

        line += [1]
        lt.append(line)

    return lt
