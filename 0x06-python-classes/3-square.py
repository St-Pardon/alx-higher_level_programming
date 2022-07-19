#!/usr/bin/python3
"""
A module for working with squares.
"""


class Square:
    """
    This represents a 2D Polygon
    with 4 equal and perpendicular sides.
    """
    def __init__(self, size=0):
        super().__init__()
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        return self.__size ** 2
