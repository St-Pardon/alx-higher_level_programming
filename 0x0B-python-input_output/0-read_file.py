#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """functions"""
    with open(filename, encoding='utf-8') as file:
        for line in file.readlines():
            print(line, end='')
