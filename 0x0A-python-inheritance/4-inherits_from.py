#!/usr/bin/python3
"""a function"""


def inherits_from(obj, a_class):
    """
    object is an instance of a class that inherited (directly or indirectly) /
    from the specified class
    """
    return issubclass(obj.__class__, a_class) and (type(obj) is not a_class)
