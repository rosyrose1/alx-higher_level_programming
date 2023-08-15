#!/usr/bin/python3
"""
Defining a file-appending function
"""


def append_write(filename="", text=""):
    """
    write_file - appends a string at the end of a text file (UTF8),
                and returns the number of characters added:
    Args:
        filename: name of the file to append to
        text: text to be written
    Return: number of bytes written.
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
