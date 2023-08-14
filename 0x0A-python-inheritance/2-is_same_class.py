#!/usr/bin/python3
""" Determine whether an object belongs to a specific type.
"""

def is_same_class(obj, a_class):
    """ Determines whether obj is of type a_class
    """
    return type(obj) == a_class
