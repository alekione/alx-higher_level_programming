#!/usr/bin/python3
"""
    search an element at a given index from
        given list
"""


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
