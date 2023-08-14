#!/usr/bin/python3
"""Defines a class Square based on 9-rectangle.py.

Attributes:
    width (int): rectangle width
    height (int): rectangle height
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square.

    Args:
        Rectangle (Rectangle): rectangle
    """

    def __init__(self, size):
        """build new instances of class Square.

        Args:
            size (int): size of 1 side of square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Copmutes the area of a square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2
