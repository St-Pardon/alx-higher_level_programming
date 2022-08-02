#!/usr/bin/python3
from json import JSONEncoder


def from_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    return JSONEncoder().decode(my_obj)
