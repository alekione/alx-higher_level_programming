#!/usr/bin/python3
""" write to a file in JSON format """
import json


def save_to_json_file(my_obj, filename):
    """  writes an Object to a text file, using a JSON representation """
    with open(filename, mode="w", encoding="UTF8") as fp:
        fp.write(json.dumps(my_obj))
