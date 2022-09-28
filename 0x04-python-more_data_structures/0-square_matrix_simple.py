#!/usr/bin/python3

# squares all elents of a 2d list matrix

def square_matrix_simple(matrix=[]):
    mat_dup = []
    for i in matrix:
        mat_dup.append(list(map(lambda x: x ** 2, i)))
    return mat_dup
