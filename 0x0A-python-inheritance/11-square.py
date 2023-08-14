#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class that defines a Square using the Rectangle class. """
    def __init__(self, size):
        """ Method responsible for initializing a Square. """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that produces a string containing the area """
        return super().area()

    def __str__(self):
        """ special method that generates a string suitable for printing """
        return "[Square] {}/{}".format(self.__size, self.__size)
