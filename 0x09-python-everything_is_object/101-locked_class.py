#!/usr/bin/python3
""" A sample of a locked class """


class LockedClass:
    """ An example of a locked class that does not allow creation of
    attributes other ths ' first_name'
    """
    __slots__ = ["first_name"]
