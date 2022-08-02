#!/usr/bin/python3
"""function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.
    """
    res = []
    with open(filename, mode='r') as file:
        for line in file.readlines():
            res.append(line)
            if line.find(search_string) >= 0:
                res.append(new_string)
    with open(filename, mode='w') as file:
        file.writelines(res)
