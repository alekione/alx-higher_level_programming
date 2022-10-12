#!/usr/bin/python3
""" square class definition """


class Square:
    """ create an square object """

    def __init__(self, size=0):
        """ Initialize object variables """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Get the area of the square """
        return self.__size * self.__size
