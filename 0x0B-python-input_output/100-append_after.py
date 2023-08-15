#!/usr/bin/python3
"""
Defining a text file insertion function.
"""


def append_after(filename="", search_string="", new_string=""):
    '''Method for inserting text after search string.'''
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        g = 0
        while g < len(lines):
            if search_string in lines[g]:
                lines[g:g + 1] = [lines[g], new_string]
                g += 1
            g += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
