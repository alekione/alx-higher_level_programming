#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last2 = ((number * -1) % 10) * -1
    last = last2
else:
    last = number % 10
    last2 = last
if last2 <= 5 and last2 != 0:
    msg = "is less than 6 and not 0"
elif last2 > 5:
    msg = "is greater than 5"
else:
    msg = "is zero"
print("Last digit of {} is {} and {}".format(number, last, msg))
