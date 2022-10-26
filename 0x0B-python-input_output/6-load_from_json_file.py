#!/usr/bin/python3
""" create obj from JSON file """
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a JSON file """
    with open(filename, mode="r") as fp:
        return json.loads(fp.read())
