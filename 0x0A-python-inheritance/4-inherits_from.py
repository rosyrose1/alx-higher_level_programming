#!/usr/bin/python3
""" Determines whether an object is in a certain class
"""


def inherits_from(obj, a_class):
    """ Verifies whether obj is an instance of a subclass derived from a_class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
