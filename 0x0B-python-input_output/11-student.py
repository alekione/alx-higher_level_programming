#!/usr/bin/python3
""" Student class definition """


class Student:
    """ create an onbject student with attributes
    first_name, last_name and age, to_json() """

    def __init__(self, first_name, last_name, age):
        """ initializes object fields """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ creates a simple dict for json creation """
        if attrs is None:
            return vars(self)
        r_dict = dict()
        for item in attrs:
            if item in vars(self):
                r_dict[item] = vars(self)[item]
        return r_dict

    def reload_from_json(self, json):
        """ replaces all attributes of students instance """
        for key, val in json:
            if key == "first_name":
                self.first_name = val
            if key == "last_name":
                self.last_name = val
            if key == "age":
                self.age = age
