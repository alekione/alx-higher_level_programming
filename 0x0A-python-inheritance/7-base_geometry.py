#!/usr/bin/python3
""" BaseGeometry class definition module """


class BaseGeometry:
    """ class attributes
    area()
    integer_validator(name, value)
    """
    def area(self):
        """ raises an exception if invoked """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
