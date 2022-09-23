#!/usr/bin/python3

"""
    print_list_integer - print elements of a list
    args:
        my_list: a list
"""


def print_list_integer(my_list=[]):
    for item in my_list:
        print("{:d}".format(item))
