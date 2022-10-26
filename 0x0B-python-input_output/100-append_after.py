#!/usr/bin/python3
""" insert a line at a specific place in a file """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line
    containing a specific string """
    n_str = ""
    with open(filename, mode="r", encoding="UTF8") as fp:
        for line in fp:
            if search_string in line:
                n_str += line + new_string
            else:
                n_str += line
    with open(filename, mode="w", encoding="UTF8") as fp:
        fp.write(n_str)
