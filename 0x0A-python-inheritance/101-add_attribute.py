#!/usr/bin/python3
""" module for adding attributes to a given objrct """


def add_attribute(obj, name, value):
    """ sets a new attribute on the given object """
    setattr(obj, name, value)
