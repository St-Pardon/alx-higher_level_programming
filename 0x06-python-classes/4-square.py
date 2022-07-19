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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        return self.size ** 2
