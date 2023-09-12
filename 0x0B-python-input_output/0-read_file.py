#!/usr/bin/python3
"""This module reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """This function created to read an input file

    Args:
        filename: the name of the file to read
    """
    with open(filename, "r", encoding= "utf-8") as file:
        for line in file:
            print(line, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-read_file.txt")
