#!/usr/bin/python3
"""Offers a function for reading and displaying the contents of a file. """


def read_file(filename=""):
    """Displays the contents of a file"""
    with open(filename, "r") as istream:
        print(istream.read(), end="")
