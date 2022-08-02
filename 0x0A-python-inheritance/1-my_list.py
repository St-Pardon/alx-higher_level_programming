#!/usr/bin/python3
"""class mode"""


class MyList(list):
    """Mylist class that inherites from list"""
    def print_sorted(self):
        """function that prints the list, but sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
        del sorted_list
