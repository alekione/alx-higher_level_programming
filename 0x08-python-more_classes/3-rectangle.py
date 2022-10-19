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

    def area(self):
        """ calculates and return the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ calculateand returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """ returns a string object of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_str = ("#" * self.__width + "\n") * self.__height
        return rec_str

    def __repr__(self):
        """ returns a canonocal string representation of the object """
        param = str(self.width) + ", " + str(self.__height)
        objct = "3-rectangle.Rectangle(" + param + ")"
        return objct
