#!/usr/bin/python3

def roman_to_int(roman_string):
    my_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
                            }
    if roman_string is None or type(roman_string) != str\
            or len(roman_string) == 0:
        return 0
    i = 0
    total = 0
    while i < len(roman_string):
        r_char = roman_string[i]
        if r_char not in my_dict:
            return 0
        if i == len(roman_string) - 1:
            return total + my_dict[roman_string[i]]
        if my_dict[r_char] < my_dict[roman_string[i + 1]]:
            total -= my_dict[r_char]
        else:
            total += my_dict[r_char]
        i += 1
