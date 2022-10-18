#!/usr/bin/python3
""" a function used for printing a name as passed to it """


def say_my_name(first_name, last_name=""):
    """ Function is used to print a name as a greetings in format;
    My name is <first name> <last name>
    Example:
    >>> say_my_name("Alex")
    My name is Alex
    >>> say_my_name("Alex", "MN")
    My name is Alex MN
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
