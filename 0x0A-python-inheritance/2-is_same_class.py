#!/usr/bin/python3
""" checks whether a given object is an instance of a given class """


def is_same_class(obj, a_class):
    """ returns True or False """
    if type(obj) == a_class:
        return True
    return False
