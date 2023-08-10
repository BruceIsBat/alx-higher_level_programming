#!/usr/bin/python3
def print_reversed_alphabet():
    for i in range(ord('z'), ord('a') - 1, -1):
        print("{}".format(chr(i)), end="")
        if i != ord('a'):
            print("{}".format(chr(i - 32)), end="")
