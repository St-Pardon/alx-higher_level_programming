#!/usr/bin/python3
"""functions"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text /
    file (UTF8) and returns the number of characters
    """
    n = 0
    with open(filename, mode='a', encoding='utf-8') as file:
        n = file.write(text)
    return n
