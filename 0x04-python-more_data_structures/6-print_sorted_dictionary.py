#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    if a_dictionary is not None:
        for pair in sorted(a_dictionary.items(), key=lambda key, *_: key):
            print('{}: {}'.format(*pair))
