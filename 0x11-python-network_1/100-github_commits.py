#!/usr/bin/python3
"""Write a Python script that takes 2 arguments
in order to solve this challenge
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys


if __name__ == "__main__":
    URL = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    reply = requests.get(URL)
    commits = reply.json()
    try:
        for s in range(10):
            print("{}: {}".format(
                commits[s].get("sha"),
                commits[s].get("commit").get("author").get("name")))
    except IndexError:
        pass
