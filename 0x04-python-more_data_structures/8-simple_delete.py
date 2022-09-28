#!/usr/bin/python3

# deletes elements from a dictionary

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
