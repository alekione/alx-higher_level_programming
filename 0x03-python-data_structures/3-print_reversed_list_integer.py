#!/usr/bin/python3

# print a list in a reverse order

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for item in my_list:
        print("{:d}".format(item))
