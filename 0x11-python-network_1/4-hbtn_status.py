#!/usr/bin/python3
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

URL = 'https://intranet.hbtn.io/status'

if __name__ == '__main__':

    resp = requests.get(URL)
    print("Body response:")
    print("\t- type:", type(resp.text))
    print("\t- content:", resp.text)
