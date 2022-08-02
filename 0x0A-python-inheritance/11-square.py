#!/usr/bin/python3
"""a class"""


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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)


class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
