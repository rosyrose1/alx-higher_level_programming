#!/usr/bin/python3
""" Defines a class to represent squares
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Definies a constant size square
    """
    def __init__(self, size):
        """ Instantiating a square
        """
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be greater than 0")
        self.__size = size

    def __str__(self):
        """ Dipict a string representation of a square
        """
        return '[Square] {size}/{size}'.format(size=self.__size)
