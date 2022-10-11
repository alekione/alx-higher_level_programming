#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
    else:
        return ret
    return None
