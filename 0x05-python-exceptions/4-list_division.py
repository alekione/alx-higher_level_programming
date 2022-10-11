#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_arr = []
    while i < list_length:
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_arr.append(res)
        i += 1
    return new_arr
