#!/usr/bin/python3
"""This module appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file (UTF8) and r

    eturns the number of characters added
    Args:
        filename: the filename
        text: the text to write
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-append_file.txt")
