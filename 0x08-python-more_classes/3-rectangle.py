#!/usr/bin/python3
""" Provides a class that represents a rectangle
"""


class Rectangle():
    """ Declares a class to represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Iitialized a rectangle
        """
        self.height = height
        self.width = width

    def __str__(self):
        """ Displays a rectangle as a string
        """
        if self.height and self.width:
            return '\n'.join(['#' * self.width] * self.height)
        return ''

    @property
    def width(self):
        """ Get the width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Place the height of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Get the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """ Get the perimeter of a rectangle
        """
        if self.width and self.height:
            return 2 * (self.width + self.height)
        return 0
