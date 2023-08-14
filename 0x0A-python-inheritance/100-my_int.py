#!/usr/bin/python3
""" Givess a rebel integer
"""


class MyInt(int):
    """ MyInt is a rebel. MyInt has == and != operators inverted.
    """
    def __eq__(self, value):
        """ Perform the opposite of ==
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """ Perform the opposite of !=
        """
        return super().__eq__(value)
