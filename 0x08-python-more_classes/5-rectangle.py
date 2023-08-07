#!/usr/bin/python3
""" Provides a class that represent a rectangle
"""


class Rectangle():
    """ Defines a class to represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Instantiate a rectangle
        """
        self.height = height
        self.width = width

    def __str__(self):
        """ Representing a rectangle as a string
        """
        if self.height and self.width:
            return '\n'.join(['#' * self.width] * self.height)
        return ''

    def __repr__(self):
        """ Representing a rectangle in a form that may be reused as input
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    @property
    def width(self):
        """ Get the width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """  the height of a rectangle
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
        """  the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """ the perimeter of a rectangle
        """
        if self.width and self.height:
            return 2 * (self.width + self.height)
        return 0
