#!/usr/bin/python3
""" prints a formatted / idented text """


def text_indentation(text):
    """ idents a string whenever ':' or '?' or '.' are found
    two new line characters are added.
    Examples:
    >>> text_identation("sleep?beauty")
    sleep
    BLANK_LINE
    beauty
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for letter in text:
        if letter in ('?', '.', ':'):
            print(letter + "\n")
        else:
            print(letter, end='')

