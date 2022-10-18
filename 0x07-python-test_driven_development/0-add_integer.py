#!/usr/bin/python3
""" a function used to add two numbers tongether"""


def add_integer(a, b=98):
    """ add two numbers tongether.
    One number is provided. Example;
    >>> add_integer(10)
    108
    >>> add_integer(10, 12)
    22
    >>> add_integer("sd", 7)
    TypeError: a must be an integer
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
