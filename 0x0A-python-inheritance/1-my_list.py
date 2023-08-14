#!/usr/bin/python3
"""
   Module inherits from list.
    """

class MyList(list):
    """
        MyList
    """
    def print_sorted(self):
        """
        Display a List that has been sorted
        """
        print(sorted(self))
