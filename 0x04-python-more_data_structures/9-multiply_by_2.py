#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    my_dict = {key: val * 2 for key, val in a_dictionary.items()}
    return my_dict
