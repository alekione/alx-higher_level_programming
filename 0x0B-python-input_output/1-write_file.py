#!/usr/bin/python3
""" write contents on a file """


def write_file(filename='', text=''):
    """ write content in text to filename and
    return number of characters written """
    with open(filename, mode="w", encoding="UTF8") as fp:
        res = fp.write(text)
    return res
