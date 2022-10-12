#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (type(position) != tuple or len(position) != 2 or
                type(position[0]) != int or type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
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
