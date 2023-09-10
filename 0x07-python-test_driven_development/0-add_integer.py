#!/usr/bin/python3
""" This module converts two argument to int then add them
"""
def add_integer(a, b=98):
    """ The function to add two floats or integers

    args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return is the sum of the two
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return (a + b)
