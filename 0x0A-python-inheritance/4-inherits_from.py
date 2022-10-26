#!/usr/bin/python3
""" checks whether the given obj belongs to a subclass of given class """


def inherits_from(obj, a_class):
    """ retuns True or False """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
