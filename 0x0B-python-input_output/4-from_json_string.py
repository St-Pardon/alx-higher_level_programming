#!/usr/bin/python3
"""function"""
from json import JSONDecoder


def from_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    return JSONDecoder().decode(my_obj)
