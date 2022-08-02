#!/usr/bin/python3
"""Class module"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value < 1:
            raise ValueError("{:s} must be greater than 0".format(name))
