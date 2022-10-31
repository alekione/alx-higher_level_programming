#!/usr/bin/python3
""" Base class initialization """


class Base:
    """ Attributes for the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize field id for all classes and objects """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
