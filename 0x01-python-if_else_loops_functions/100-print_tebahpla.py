#!/usr/bin/python3
def print_reversed_alphabet():
    for i in range(90, 64, -1):
        char1 = chr(i + 32)
        char2 = chr(i)
        print(f"{char1}{char2}", end="")
