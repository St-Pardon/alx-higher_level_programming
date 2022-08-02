#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class."""
    return type(obj) is a_class
