#!/usr/bin/python3
""" creates a pascal triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    m_list = [[1]]
    sub_list = [1]
    for i in range(n - 1):
        res = []
        for j in range(len(sub_list) + 1):
            if j == 0 or j == len(sub_list):
                res.append(1)
            else:
                res.append(sub_list[j] + sub_list[j - 1])
        sub_list = res
        m_list.append(res)
    return m_list
