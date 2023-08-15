#!/usr/bin/python3
"""Declares a class Student."""


class Student:
    """Dipict a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): Name of the first student.
            last_name (str): Name of the last student.
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
