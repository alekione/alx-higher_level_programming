#!/usr/bin/python3
for i in range(100):
    if (i == 89):
        print("{:d}".format(i))
        break
    if (i < 10):
        print("{:02d}".format(i), end=', ')
    else:
        if (i % 10) <= (i // 10):
            continue
        print("{:d}".format(i), end=', ')
