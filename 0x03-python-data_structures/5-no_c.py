#!/usr/bin/python3

# removes characters 'c' and 'C' on a given string

def no_c(my_string):
    n_str = ""
    for c in my_string:
        if c not in "cC":
            n_str += c
    return n_str
