#!/usr/bin/python3

# print Fizz Buzz rythym

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("{}".format("FizzBuzz"), end=' ')
        elif i % 5 == 0:
            print("{}".format("Buzz"), end=' ')
        elif i % 3 == 0:
            print("{}".format("Fizz"), end=' ')
        else:
            print("{}".format(i), end=' ')
