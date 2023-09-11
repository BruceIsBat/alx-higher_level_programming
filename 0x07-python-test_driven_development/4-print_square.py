#!/usr/bin/python3
"""This module prints a square with the character #
"""


def print_square(size):
    """ function that prints a square with the character #

    Args:
        size: integer value

    Return:
        returns none
    """
    try:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            for first in range(size):
                for second in range(size):
                    print("#", end='')
                print()
    except TypeError as e:
        print(e)
    except ValueError as r:
        print(r)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
