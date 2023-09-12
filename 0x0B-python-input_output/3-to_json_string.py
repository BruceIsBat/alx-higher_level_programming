#!/usr/bin/python3
"""This module returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """function returns the JSON representation of an object (string)

    Args:
        my_obj: argument taken
    """
    import json
    return json.dumps(my_obj)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-to_json_string.txt")
