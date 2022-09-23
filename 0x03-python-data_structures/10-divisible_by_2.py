#!/usr/bin/python3

# checks if a number is divisible by 2 and appends a bool result on a list

def divisible_by_2(my_list=[]):
    n_list = []
    for item in my_list:
        if item % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list
