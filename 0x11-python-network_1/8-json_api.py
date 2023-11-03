#!/usr/bin/python3
'''
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

import requests
import sys

URL = 'http://0.0.0.0:5000/search_user'

if __name__ == '__main__':

    data = {'q': '' if len(sys.argv) == 1 else sys.argv[1]}
    reply = requests.post(URL, data=data)
    try:
        json = reply.json()
    except ValueError:
        print('Not a valid JSON')
    else:
        if json:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
