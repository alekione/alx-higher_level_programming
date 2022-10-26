#!/usr/bin/python3
""" Rectangle class definition """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits/extends the deometry class """

    def __init__(self, width, height):
        """ initializes object fields """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
