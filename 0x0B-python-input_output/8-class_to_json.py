#!/usr/bin/python3
""" converts an object into a json data """


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    for JSON serialization of an object """
    var1 = {k: v for k, v in type(obj).__dict__.items()
            if not k.startswith("__")
            and not k.endswith("__")
            and "method" not in str(v)
            and "function" not in str(v)}
    return dict(vars(obj).items() | var1.items())
