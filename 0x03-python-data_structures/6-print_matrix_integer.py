#!/usr/bin/python3

# prints elements of a matrix- list.

def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        ind = 0
        for item in lst:
            if ind == len(lst) - 1:
                print("{:d}".format(item))
            else:
                print("{:d}".format(item), end=' ')
            ind += 1
