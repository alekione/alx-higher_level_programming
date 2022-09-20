#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = ((number * -1) % 10) * -1
else:
    last = number % 10
if last <= 5 and last != 0:
    msg = "is less than 6 and not 0"
elif last > 5:
    msg = "is greater than 5"
else:
    msg = "is zero"
print("Last digit of {} is {} and {}".format(number, last, msg))
