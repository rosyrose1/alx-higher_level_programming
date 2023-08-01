#!/usr/bin/python3
""" Defining a class 'Square'
"""
class Square():
    """ Calculates the area of a 'Square'
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
        """ Finds the area of a 'Square'
        """
        return self.__size ** 2
