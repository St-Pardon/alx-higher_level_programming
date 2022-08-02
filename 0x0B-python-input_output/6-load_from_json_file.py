#!/usr/bin/python3
"""function"""
from json import JSONDecoder


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    lines = []
    with open(filename, encoding='utf-8') as file:
        for line in file.readlines():
            lines.append(line)
    return JSONDecoder().decode(''.join(lines))
