#!/usr/bin/python3
""" Provides a class that represent a rectangle
"""


class Rectangle():
    """ Defining a class to represent a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Instantiate a rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __del__(self):
        """ Delete a rectangle
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """ Represent a rectangle as a string
        """
        if self.height and self.width:
            return '\n'.join(
                [str(self.print_symbol) * self.width] * self.height
            )
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
        """ Place the width of a rectangle
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
        """ Set the height of a rectangle
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Get the larger rectangle (rect_1 if they have equal area)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Get a new rectangle with width equal to height
        """
        return cls(size, size)