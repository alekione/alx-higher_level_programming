#!/usr/bin/python3
""" MyInt class definition """


class MyInt(int):
    """ class extends int class and inverses == with != """

    def __eq__(self, other):
        """ checks whether the objects are equal """
        return int(self) != other

    def __ne__(self, other):
        """ checks whether the objects are not equal """
        return int(self) == other
