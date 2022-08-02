#!/usr/bin/python3
"""class module"""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if '__dict__' in dir(self):
            res = dict()
            found = False
            if (type(attrs) is list) and all(type(s) is str for s in attrs):
                found = True
            for key in self.__dict__.keys():
                if (not found) or (found and key in attrs):
                    res[key] = self.__dict__[key]
            return res

    def reload_from_json(self, json):
        if isinstance(json, dict) and ('__dict__' in dir(self)):
            for key in json.keys():
                self.__dict__[key] = json[key]
