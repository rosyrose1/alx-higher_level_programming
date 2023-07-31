#!/usr/bin/python3
def safe_print_division(a, b):
    """ Dividing the two integers """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        try:
            print("Inside result: {}".format(result))
        except NameError:
            pass
    return result
