#!/usr/bin/python3
from magic_calculation_102 import add, sub
def magic_calculation(a, b):
    if a < b:
        c = a + b
        for i in range(90):
            c = add(c, i)
        return c

    return sub(a, b)
