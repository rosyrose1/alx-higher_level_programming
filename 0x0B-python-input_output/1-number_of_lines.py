#!/usr/bin/python3
def number_of_lines(filename=""):
    """ A function that provides the count of lines in a text file. """
    with open(filename, encoding='utf-8') as f:
        return(len(f.readlines()))
