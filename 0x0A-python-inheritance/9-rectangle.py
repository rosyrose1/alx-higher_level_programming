#!/usr/bin/python3
""" Offers a class for the representation of rectangles.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Description of a rectangle with a constant size.
    """
    def __init__(self, width, height):
        """ Instantiate a rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Display a textual portrayal of a rectangle.
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self):
        """ Compute the area of a rectangle
        """
        return self.__width * self.__heighti
