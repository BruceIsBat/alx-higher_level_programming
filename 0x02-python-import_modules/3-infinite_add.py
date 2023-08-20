#!/usr/bin/python3
import sys


def main():
    b = 0
    for i in range(1, len(sys.argv)):
        a = int(sys.argv[i])
        b += a
    print("{}".format(b))


if __name__ == "__main__":
    main()
