#!/usr/bin/python3
"""functions"""
from json import JSONEncoder


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    return JSONEncoder().encode(my_obj)
