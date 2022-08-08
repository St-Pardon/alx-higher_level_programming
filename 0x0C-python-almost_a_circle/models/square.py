#!/usr/bin/python3
"""square module"""
from .rectangle import Rectangle


class Square(Rectangle):
    """creates squares"""
    def __init__(self, size, x=0, y=0, id=None):
        """init the square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return '[Square] ({}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kargs):
        """Updates the attributes"""
        keys = ('id', 'size', 'x', 'y')
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
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return result
