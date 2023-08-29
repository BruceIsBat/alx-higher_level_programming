#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
        print("Inside result: {}".format(result))
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        if 'result' in locals():
            return (result)
        else:
            result = None
            return (result)
