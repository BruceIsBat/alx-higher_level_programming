#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            g = my_list[i]
            print("{}".format(g), end=(""))
        print()
        return (g)
    except IndexError:
        print()
        return (g)
    finally:
        if 'g' in locals():
            return (g)
        else:
            return (0)
