#!/usr/bin/python3
"""This module works on a Square class which takes in parameters
"""


class Square():
    """
    This is a class Square that defines a square

    This class can be used as a starting point for creating new classes
    or as a placeholder for future development.

    Example usage:
        emp = Square()

    Attributes:
        size: the size of the square sides defaults to 0

    Methods:
        size: the size of the square sides defaults to 0
    Args:
        size: the size of the square sides defaults to 0

    """
    def __init__(self, size=0):
        """The  __init__ method for the class Square.

        The init method takes in a protected parameter size defaulted to 0

        Args:
            size: the size of the square sides defaults to 0

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
