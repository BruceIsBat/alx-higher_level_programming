#!/usr/bin/python3
import dis


def print_defined_names(module_name):
    module = __import__(module_name)
    names = sorted(dir(module))
    for name in names:
        if not name.startswith('__'):
            print(name)


if __name__ == "__main__":
    print_defined_names("hidden_4")
