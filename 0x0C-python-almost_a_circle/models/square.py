#!/usr/bin/python3
""" definition on square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Attributes of th class aquare tha extends Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes square fields """
        self.__size = size
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """ returns a string representation of the object """
        return f"[Square] {(self.id)} {super().x()}/{super().y()} - {super().height()}"
