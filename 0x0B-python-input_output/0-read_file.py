#!/usr/bin/python3
""" reads contents of a file """


def read_file(filename=''):
    """ read a file and print it to stdout """
    with open(filename, encoding='utf-8') as fp:
        print(fp.read())
