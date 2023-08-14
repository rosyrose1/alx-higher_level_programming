#!/usr/bin/python3
"""
    modules inherit from list
    """


class MyList(list):
    """
        MyList
    """
    def print_sorted(self):
        """
        Display a list that has been sorted
        """
        print(sorted(self))
