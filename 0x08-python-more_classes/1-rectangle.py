#!/usr/bin/python3
""" A class that is used to create a rectangle object """


class Rectangle:
    """ Attributes for creating a rectangle class
    width - width of the rectangle
    height - height of the rectangle
    getters - width()
                        height()
    setters - width(val)
                        height(val)
    """

    def check_vals(self, width, height):
        """ checks whether the values passed to the object
        meets the requirements
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def __init__(self, width=0, height=0):
        """ initialize object field """
        self.check_vals(width, height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter of the field - width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the field - width """
        self.check_vals(value, 0)
        self.__width = value

    @property
    def height(self):
        """ getter of the field - height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for field - height """
        self.check_vals(0, value)
        self.__height = value
