#!/usr/bin/python3
class Square:
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
