#!/usr/bin/python3
'''
A module for working with squares.
'''


class Square:
    '''
    this represents a 2D Polygon
    with 4 equal and perpendicular sides.
    '''
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

    def __eq__(self, value):
        if isinstance(value, Square):
            return self.area() == value.area()
        else:
            return False

    def __ne__(self, value):
        if isinstance(value, Square):
            return self.area() != value.area()
        else:
            return True

    def __gt__(self, value):
        if isinstance(value, Square):
            return self.area() > value.area()
        else:
            err_msg = "'>' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __ge__(self, value):
        if isinstance(value, Square):
            return self.area() >= value.area()
        else:
            err_msg = "'>=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __lt__(self, value):
        if isinstance(value, Square):
            return self.area() < value.area()
        else:
            err_msg = "'<' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __le__(self, value):
        if isinstance(value, Square):
            return self.area() <= value.area()
        else:
            err_msg = "'<=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False
