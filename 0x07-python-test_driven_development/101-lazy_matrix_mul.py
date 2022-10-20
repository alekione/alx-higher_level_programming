#!/usr/bin/python3
""" a module for multiplying matrixes  using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplies a list matrix with another list matrix
    m_a * m_b
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for item in m_a:
        if type(item) != list:
            raise TypeError("m_a must be a list of lists")
        size = len(m_a[0])
        if len(item) == 0:
            raise ValueError("m_a can't be empty")
        if len(item) != size:
            raise TypeError("each row of m_a must be of the same size")
        for num in item:
            if type(num) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for item in m_b:
        if type(item) != list:
            raise TypeError("m_b must be a list of lists")
        if len(item) == 0:
            raise ValueError("m_b can't be empty")
        size = len(m_b[0])
        if len(item) != size:
            raise TypeError("each row of m_b must be of the same size")
        for num in item:
            if type(num) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.matmul(m_a, m_b)
