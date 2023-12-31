#!/usr/bin/python3
""" Naming of a class 'Square'
"""


class Square():
    """ Compute the area of a 'Square'
    """
    def __init__(self, size=0):
        """ Instantiate a 'Square'
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ aquires the area of a 'Square'
        """
        return self.__size ** 2
