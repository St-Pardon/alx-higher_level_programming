#!/usr/bin/python3
'''
A module for working with singly linked lists.
'''


class Square:
    '''
    this represents a node in a singly linked list.
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    @position.setter
    def position(self, value):
        is_invalid_value = True
        error_msg = 'position must be a tuple of 2 positive integers'
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        is_invalid_value = False
        if is_invalid_value:
            raise TypeError(error_msg)
        else:
            self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print('\n')
        else:
            print('{}'.format('\n' * self.position[1]), end='')
            for i in range(self.size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.size))

    def __str__(self):
        res = []
        if self.size == 0:
            res.append('')
        else:
            if self.position[1] > 0:
                res.append('{}'.format('\n' * (self.position[1] - 1)))
            for i in range(self.size):
                res.append('{}{}'.format(
                    ' ' * self.position[0],
                    '#' * self.size))
        return '\n'.join(res)
