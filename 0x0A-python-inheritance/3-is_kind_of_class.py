#!/usr/bin/python3
""" checks whether an object is an instance of, or,
if the object is an instance of a class that is inherited from """


def is_kind_of_class(obj, a_class):
    """ returns True or False """
    return isinstance(obj, a_class)
