#!/usr/bin/python3

# remove a char at a given index and return a copy

def remove_char_at(str, n):
    s = ""
    i = 0
    while i < len(str):
        if i != n:
            s += str[i]
        i += 1
    return s
