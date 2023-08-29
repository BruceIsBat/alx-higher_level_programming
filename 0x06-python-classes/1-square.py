#!/usr/bin/python3
""" This module Private instance attribute: size
"""


class Square():
    """
    This is a class Square that defines a square

    This class can be used as a starting point for creating new classes
    or as a placeholder for future development.

    Example usage:
        emp = Square()

    Attributes:
        size: the size of the square sides

    Methods:
        size: the size of the square sides
    Args:
        size: the size of the square sides
    """
    def __init__(self, size):
        """The  __init__ method for the class Square.

        The init method takes in a protected parameter size

        Args:
            size: the size of the square sides
        """
        self.__size = size
