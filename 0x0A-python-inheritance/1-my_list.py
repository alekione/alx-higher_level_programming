#!/usr/bin/python3
""" module that defines a class mylist """


class MyList(list):
    """ class MyList extends list class.
    Attributes:
        print_sorted()
    """
    def print_sorted(self):
        """ prints a sorted list"""
        print(sorted(self))
