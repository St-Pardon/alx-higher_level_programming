#!/usr/bin/python3
"""class module"""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if '__dict__' in dir(self):
            return self.__dict__
