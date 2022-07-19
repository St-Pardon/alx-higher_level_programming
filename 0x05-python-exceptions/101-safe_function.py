#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: ")
        sys.stderr.write(err.args[0])
        sys.stderr.write("\n")
        return None
