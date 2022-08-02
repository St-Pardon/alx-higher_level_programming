#!/usr/bin/python3
"""class module"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value < 1:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
