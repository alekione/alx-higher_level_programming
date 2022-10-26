#!/usr/bin/python3
""" reads contents of a file """


def read_file(filename=''):
    """ read a file and print it to stdout """
    with open(filename, mode="r", encoding='UTF8') as fp:
        for line in fp:
            print (line)
