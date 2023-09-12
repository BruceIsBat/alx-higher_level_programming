#!/usr/bin/python3
"""This module writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)

    returns the number of characters written
    Args:
        filename: the filename
        text: the text to write
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-write_file.txt")
