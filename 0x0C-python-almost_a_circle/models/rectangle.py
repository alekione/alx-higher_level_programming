#!/usr/bin/python3
""" Initialization of a Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ initialization of object attributes """

    def check_val(self, **kwargs):
        """ checks whether the values passed for width and height
        meets the requirements """
        for item, val in kwargs.items():
            if type(val) != int:
                raise TypeError(f"{item} must be an integer")
            if (item == "x" or item == "y" or item == "id") and val >= 0:
                continue
            if val < 0:
                if item == "x" or item == "y" or item == "id":
                    raise ValueError(f"{item} must be >= 0")
                else:
                    raise ValueError(f"{item} must be > 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization of object fields """
        self.check_val(width=width, height=height, x=x, y=y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ returns the width of the object """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets a new value to the field width """
        self.check_val(width=value, height=0)
        self.__width = value

    @property
    def height(self):
        """ returns the height of the object """
        return self.__height

    @height.setter
    def height(self, value):
        """ changes the value of height """
        self.check_val(width=0, height=value)
        self.__height = value

    @property
    def x(self):
        """ returns the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets a new value for x """
        self.check_val(x=value, y=0)
        self.__x = value

    @property
    def y(self):
        """ returns the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets a new value for y """
        self.check_val(x=0, y=value)
        self.__y = value

    def update(self, *args, **kwargs):
        """ updates field values """
        i = 0
        if args is None or len(args) == 0:
            if kwargs is not None:
                for item, val in kwargs.items():
                    if item == "id":
                        self.check_val(id=val)
                        self.id = val
                    if item == "width":
                        self.check_val(width=val)
                        self.__width = val
                    if item == "height":
                        self.check_val(height=val)
                        self.__height = val
                    if item == "y":
                        self.check_val(y=val)
                        self.__y = val
                    if item == "x":
                        self.check_val(x=val)
                        self.__x = val
        if args is None or len(args) == 0:
            return
        for item in args:
            if i == 0:
                self.check_val(id=item)
                self.id = item
            if i == 1:
                self.check_val(width=item)
                self.__width = item
            if i == 2:
                self.check_val(height=item)
                self.__height = item
            if i == 3:
                self.check_val(x=item)
                self.__x = item
            if i == 4:
                self.check_val(y=item)
                self.__y = item
            i += 1

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle using # character """
        r_str = '\n' * self.__y
        r_str += (((' ' * self.__x + '#' * self.__width) + '\n') *
                  self.__height)
        print(r_str[:-1])

    def __str__(self):
        """ returns a string representation of the object """
        id = self.id
        height = self.__height
        width = self.__width
        return f"[Rectangle] ({id}) {self.__x}/{self.__y} - {width}/{height}"
