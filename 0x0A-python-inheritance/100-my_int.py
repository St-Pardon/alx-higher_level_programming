#!/usr/bin/python3
"""class model"""


class MyInt(int):
    '''Represents a rebellious integer object.
    '''
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
