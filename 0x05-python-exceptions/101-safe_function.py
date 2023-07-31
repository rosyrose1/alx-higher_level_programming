#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exc:
        print('Exception:', exc, file=__import__('sys').stderr)
        return None
