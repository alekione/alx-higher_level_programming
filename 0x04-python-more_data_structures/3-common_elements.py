#!/usr/bin/python3

# returns a set of common elements on 2 sets

def common_elements(set_1, set_2):
    my_set = {x for x in set_1 if x in set_2}
    return my_set
