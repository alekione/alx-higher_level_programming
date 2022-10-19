#!/usr/bin/python3
""" a function for dividing a matrix of numbers """


def matrix_divided(matrix, div):
    """ matrix - list of lists of numbers
    @div: number to divide
    divides each number of the matrix by div
    >>> matr = [[2, 4, 6], [2, 4, 6]]
    >>> matrix_divided(matr, 2)
    [[1, 2, 3], [1, 2, 3]]
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix" +
                        " (list of lists) of integers/floats")
    try:
        length = len(matrix[0])
    except IndexError:
        return list(matrix)
    new_matrix = []
    for item in matrix:
        if type(item) != list:
            raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats")
        if len(item) != length:
            raise TypeError("Each row of the matrix must have the same size")
        inner = []
        for num in item:
            if type(num) not in (int, float):
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")
            inner.append(round(num / div, 2))
        new_matrix.append(inner)
    return new_matrix
