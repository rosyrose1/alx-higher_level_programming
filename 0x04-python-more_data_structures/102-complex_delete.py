#!/usr/bin/python3


def complex_delete(a_dictionary, value):

    if a_dictionary:
        for m, p in list(a_dictionary.items()):
            if p == value:
                del a_dictionary[m]
    return a_dictionary
