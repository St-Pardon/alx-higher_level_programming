#!/usr/bin/python3
"""function"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and returns the /
    number of characters written
    """
    n = 0
    with open(filename, mode='w', encoding='utf-8') as file:
        n = file.write(text)
    return n
