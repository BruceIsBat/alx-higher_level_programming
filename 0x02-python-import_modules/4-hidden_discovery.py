#!/usr/bin/python3
import dis


def print_defined_names():
    code = __import__("hidden_4").__code__
    names = code.co_names
    filtered_names = sorted(filter(lambda name: not name.startswith('__'), names))
    for name in filtered_names:
        print(name)


if __name__ == "__main__":
    print_defined_names()
