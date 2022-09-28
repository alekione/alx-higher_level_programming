#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total1 = 0
    total2 = 0
    for i in my_list:
        total1 += i[0] * i[1]
        total2 += i[1]
    return total1 / total2
