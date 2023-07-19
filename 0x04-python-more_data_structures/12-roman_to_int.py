#!/usr/bin/python3


def _reduce(fn, seq, init=0):
    """ Reduce a list to a single value
    """
    try:
        return _reduce(fn, seq[1:], fn(init, seq[0]))
    except IndexError:
        return init


def roman_to_int(roman_string):
    """ Converting a Roman numeral to an integer
    """
    n2n = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
    }
    try:
        numbers = list(map(n2n.get, roman_string[::-1]))
        integer = numbers[0]
    except (IndexError, KeyError, TypeError):
        return 0

    for r in range(len(numbers[1:])):
        if numbers[r + 1] >= numbers[r]:
            integer += numbers[r + 1]
        else:
            integer -= numbers[r + 1]

    return integer
