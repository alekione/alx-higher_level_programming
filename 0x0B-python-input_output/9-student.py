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

    def to_json(self):
        """ creates a simple dict for json creation """
        return vars(self)
