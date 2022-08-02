#!/usr/bin/python3
"""A module for manipulating objects."""


def add_attribute(obj, name, value):
    if ('__dict__' in dir(obj)) and (type(obj.__dict__) is dict):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
