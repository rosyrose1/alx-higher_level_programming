#!/usr/bin/python3
""" Retrieve details regarding object attributes and methods.
"""

def lookup(obj):
"""Obtain a list of attributes and methods belonging to an object.
"""
return dir(obj)
