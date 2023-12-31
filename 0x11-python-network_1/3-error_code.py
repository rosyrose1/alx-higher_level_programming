#!/usr/bin/python3
'''
sends a request to the URL
and displays the body of the response (decoded in utf-8).
'''
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as r:
            print(r.read().decode())
    except HTTPError as exc:
        print('Error code:', exc.code)
        sys.exit(1)
