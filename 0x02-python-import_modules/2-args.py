#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    nargs = len(argv) - 1

    if nargs == 0:
        print("0 arguments.")
    elif nargs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nargs))

    for m, v in enumerate(argv[1:]):
        print("{}: {}".format(m + 1, v))
