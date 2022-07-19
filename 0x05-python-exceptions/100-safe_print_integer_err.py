#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        sys.stderr.write("Exception: ")
        sys.stderr.write(err.args[0])
        sys.stderr.write("\n")
        return False
