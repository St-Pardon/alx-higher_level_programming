#!/usr/bin/python3
'''A module that restrict dynamic instance creation'''


class LockedClass:
    '''class with restricted attribute modification.'''
    __slots__ = ['first_name']
