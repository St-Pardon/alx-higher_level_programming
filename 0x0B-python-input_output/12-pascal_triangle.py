#!/usr/bin/python3
"""function"""


def pascal_triangle(n):
    """
    Generates a list of lists of integers representing the
    Pascal’s triangle of a given integer.
    """
    res = []
    if n <= 0:
        return res
    for i in range(n):
        row = []
        for j in range(i + 1):
            top_left = 1 if i == 0 else 0
            top_right = 0
            if (i > 0) and (j > 0):
                top_left = res[i - 1][j - 1]
            if (i > 0) and (j < len(res[i - 1])):
                top_right = res[i - 1][j]
            row.append(top_left + top_right)
        res.append(row)
    return res
