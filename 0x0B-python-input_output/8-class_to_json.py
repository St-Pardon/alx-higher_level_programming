#!/usr/bin/python3
"""function"""


def class_to_json(obj):
    """
    function that returns the dictionary description /
    with simple data structure (list, dictionary, string, /
    integer and boolean) for JSON serialization of an object
    """
    if '__dict__' in dir(obj):
        return obj.__dict__
