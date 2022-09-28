#!/usr/bin/python3

# prints a sorted dict

def print_sorted_dictionary(a_dictionary):
    my_tple = sorted(a_dictionary.items())
    for key, val in my_tple:
        print(key + ':', val)
