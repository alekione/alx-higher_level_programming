#!/usr/bin/python3
""" square class definition """


class Square:
    """ object attributes """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize object variables
        __size(int)
        __position(tuple)
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (type(position) != tuple or len(position) != 2 or
                type(position[0]) != int or type(position[1]) != int or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """ returns the size of the square """
        return self.__size

    @property
    def position(self):
        """ returns the position values """
        return self.__position

    @size.setter
    def size(self, value):
        """ sets the size of the square """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ set the position values """
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ prints the square wit  '#' """
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            for h in range(0, self.__position[1]):
                print()
        for i in range(0, self.__size):
            if self.__position[0] > 0:
                for j in range(0, self.__position[0]):
                    print(" ", end='')
            for k in range(0, self.__size):
                print("#", end='')
            print()
