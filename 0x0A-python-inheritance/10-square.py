#!/usr/bin/python3
""" Square class definition """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class that extends Rectangle class"""

    def __init__(self, size):
        """ initializes object attributes """
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
