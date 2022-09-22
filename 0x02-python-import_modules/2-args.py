#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    else:
        if length == 1:
            print(f"{length} argument:")
        else:
            print(f"{length} arguments:")
        i = 0
        for item in sys.argv:
            if (i > 0):
                print("{}: {}".format(i, item))
            i += 1
