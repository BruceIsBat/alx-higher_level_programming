#!/usr/bin/python3
"""This module json file
"""
import json


def from_json_string(my_str):
    """This function from json
    Args:
        my_str: the string
    """
    return json.loads(my_str)


if __name__ == "__main__":
    import doctest
    doctest.textfile("4-from_json_string.txt")
