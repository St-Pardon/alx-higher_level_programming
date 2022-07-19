#!/usr/bin/python3
"""
A module for working with squares.
"""


class Square:
    """
    this rpresents a 2D Polygon
    with 4 equal and perpendicular sides.
    """
    def __init__(self, size):
        super().__init__()
        self.__size = size
