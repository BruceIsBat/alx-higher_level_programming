#!/usr/bin/python3
"""This module contains a function that prints name
"""


def say_my_name(first_name, last_name=""):
    """Function with two argument, check and return name

    Args:
        first_name: first name
        last_name: last name

    Return:
        Prints the names
    """
    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        elif not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        else:
            print(f"My name is {first_name} {last_name}")
    except TypeError as  e:
        print(e)


if __name == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
