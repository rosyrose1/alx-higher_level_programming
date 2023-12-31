#!/usr/bin/python3
"""gives  a class to represent a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle
    """
    HEADERS = ('id', 'width', 'height', 'x', 'y')

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiating a rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Acquires a string representation of a rectangle
        """
        return "[{type}] ({id}) {x}/{y} - {width}/{height}".format(
            type=self.__class__.__name__,
            id=self.id,
            width=self.__width,
            height=self.__height,
            x=self.__x,
            y=self.__y
        )

    @property
    def width(self):
        """Acquires private instance attribute 'width'
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Place private instance attribute 'width'
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Acquires private instance attribute 'height'
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Place  private instance attribute 'height'
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Acquires private instance attribute 'x'
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Place private instance attribute 'x'
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Acquires private instance attribute 'y'
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Set private instance attribute 'y'
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Displays a text representation of a rectangle
        """
        print("\n" * self.__y, end="")
        print("\n".join([" " * self.__x + "#" * self.__width] * self.__height))

    def to_dictionary(self):
        """Get a dictionary representation of  rectangle
        """
        return {key: getattr(self, key) for key in self.__class__.HEADERS}

    def update(self, *args, **kwargs):
        """Revise the attributes of object
        """
        if args:
            for pair in zip(self.HEADERS, args):
                setattr(self, *pair)
        else:
            for key in kwargs:
                if key in self.HEADERS:
                    setattr(self, key, kwargs[key])
