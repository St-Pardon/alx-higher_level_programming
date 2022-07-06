#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for i in keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
