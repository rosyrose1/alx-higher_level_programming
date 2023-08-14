#!/usr/bin/python3
""" Offers a function for appending an attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """ Attempt to add an attribute to an object
    """
    if getattr(obj, '__dict__', None) is None:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
