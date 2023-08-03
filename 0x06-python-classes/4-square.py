#!/usr/bin/python3
""" Library  a definition of a class 'Square'
"""


class Square():
    """ Specifiying a 'Square'
    """
    def __init__(self, size=0):
        """ Initiation of a 'Square'
        """
        self.size = size

    @property
    def size(self):
        """ acqiure the size of a square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ put the size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Compute the area of a 'Square'
        """
        return self.__size ** 2
