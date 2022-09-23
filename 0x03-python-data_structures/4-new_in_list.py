#!/usr/bin/python3

# creates a new list and changes an element at the given index

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
