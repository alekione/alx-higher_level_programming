#!/usr/bin/python3

"""
    return the last digit of a given number
"""


def print_last_digit(number):
    if number < 0:
        num = (number * -1) % 10
    else:
        num = number % 10
    print("{:d}".format(num), end='')
    return num
