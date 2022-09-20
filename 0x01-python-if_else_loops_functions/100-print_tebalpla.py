#!/usr/bin/python3

# print a character

def print_var(var):
    print("{:c}".format(var), end='')


for i in range(26):
    if i % 2 == 0:
        print_var(ord('z') - i)
    else:
        print_var(ord('Z') - i)
