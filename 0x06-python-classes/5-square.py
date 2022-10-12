#!/usr/bin/python3
""" square class definition """


class Square:
    """ square object creation """
    def __init__(self, size=0):
        """ Initializes object attributes
        __size(int) - size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ get the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of the square """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ prints the square with '#' """
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()
