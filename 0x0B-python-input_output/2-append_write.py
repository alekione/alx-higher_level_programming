#!/usr/bin/python3
""" append contents on a file """


def append_write(filename='', text=''):
    """ append content in text to filename and
    return number of characters written """
    with open(filename, mode="a", encoding="UTF8") as fp:
        res = fp.write(text)
    return res
