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

    def area(self):
        """ return the area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns a string rep of the object """
        return f"[Rectangle] {self.__width}/{self.__height}"
