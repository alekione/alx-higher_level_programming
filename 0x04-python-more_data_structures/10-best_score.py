#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.items()) == 0:
        return None
    t_score = 0
    for key, val in a_dictionary.items():
        if val > t_score:
            t_score = val
    for key, val in a_dictionary.items():
        if val == t_score:
            return key
