#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = a + b
        for i in range(90):
            c = add(c, i)
        return c
    else
        return sub(a, b)