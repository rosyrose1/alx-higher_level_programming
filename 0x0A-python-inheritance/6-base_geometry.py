#!/usr/bin/python3
""" Supplies a foundational class for geometric objects,
    which is primarily empty.
"""


class BaseGeometry:
    """ Execute a base class for geometric objects
    """
    def area(self):
        """ Copmute the area of a geometric object
        """
        raise Exception("area() is not implemented")
