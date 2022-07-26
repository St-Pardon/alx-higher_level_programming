#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>"""

    if not first_name or type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
