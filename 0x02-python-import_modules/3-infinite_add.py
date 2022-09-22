#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    ind = 0
    for item in sys.argv:
        if ind > 0:
            total += int(item)
        ind += 1
    print(total)
