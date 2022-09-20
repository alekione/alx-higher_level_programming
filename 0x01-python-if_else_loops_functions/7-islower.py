#!/usr/bin/python3
"""
    islower - checks whether a character is a lowercase
    c: character
    Return: True or False
"""


def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if ord(c) == i:
            return True
    return False
