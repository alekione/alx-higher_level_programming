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
            if val <= 0:
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
        self.check_val(width=value)
        self.__width = value

    @property
    def height(self):
        """ returns the height of the object """
        return self.__height

    @height.setter
    def height(self, value):
        """ changes the value of height """
        self.check_val(height=value)
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
        """updates the value of the instance
        """
        arr = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) > len(arr):
            return
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, arr[i], args[i])
            return
        if kwargs is not None:
            for key, value in kwargs.items():
                if key in arr:
                    setattr(self, key, value)

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

    def to_dictionary(self):
        """ creates a dictionary rep of the object """
        a_lst = ["id", "width", "height", "x", "y"]
        return {a_lst[i]: getattr(self, a_lst[i]) for i in range(len(a_lst))}
