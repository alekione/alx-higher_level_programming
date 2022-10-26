#!/usr/bin/python3
""" adds item to a json file """
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    with open("add_item.json", "r", encoding="UTF8") as fp:
        pass
except Exception:
    with open("add_item.json", "w", encoding="UTF8") as fp:
        pass
    save_to_json_file(sys.argv[1:], "add_item.json")
else:
    lst = load_from_json_file("add_item.json")
    lst.extend(sys.argv[1:])
    save_to_json_file(lst, "add_item.json")
