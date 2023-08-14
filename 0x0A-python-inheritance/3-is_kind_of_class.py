#!/usr/bin/python3
"""Determines whether ab object is in a certain class
"""


def is_kind_of_class(obj, a_class):
    """Determines whether obj's type is either a_class or a subclass of a_class
    """
    return isinstance(obj, a_class)
