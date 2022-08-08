#!/usr/bin/python3
'''Rectangle from Base'''
from models.base import Base


class Rectangle(Base):
    """Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """sets the x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """sets the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """reperesentation of text"""
        print('\n' * self.y, end='')
        print('{:s}{:s}\n\
'.format(' ' * self.x, '#' * self.width) * self.height, end='')

    def __str__(self):
        """string representation"""
        return "[Rectangle] ({}) {:d}/{:d} - \
{:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kargs):
        """update attributes"""
        keys = ('id', 'width', 'height', 'x', 'y')
        for key, val in zip(keys, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kargs) is dict):
            for key, val in kargs.items():
                if key in keys:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Creates a dictionary representation"""
        result = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return result
