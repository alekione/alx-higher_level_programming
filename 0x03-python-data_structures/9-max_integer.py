#!/usr/bin/python3

# searches and returns the largest value/number on a list

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    v_max = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > v_max:
            v_max = my_list[i]
        i += 1
    return v_max
