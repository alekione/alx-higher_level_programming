#!/usr/bin/python3
"""initialization of square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """attributes of Square class - inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class instance of object fields """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """handles the print of this class
        Returns:
            str: custom print string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """returns the value of size
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """setter for the size
        Args:
            value (int): the value to be set
        """
        super().update(width=value, height=value)
        self.__size = value

    def update(self, *args, **kwargs):
        """updates the value of the instance
        """
        arr = ["id", "size", "x", "y"]
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

    def to_dictionary(self):
        """returns the dictionary representation of a square
        Returns:
            dict: dictionary containing the square details
        """
        arr = ["id", "size", "x", "y"]
        return {arr[i]: getattr(self, arr[i]) for i in range(len(arr))}
