#!/usr/bin/python3
""" a function for printing a square using the # character """


def print_square(size):
    """ prints a square with the given length-size
    The square is filled with '#'
    Example:
    >>> print_square(2)
    ##
    ##
    >>> print_square(3)
    ###
    ###
    ###
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
