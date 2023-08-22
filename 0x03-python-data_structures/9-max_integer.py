#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in range(len(my_list)-1):
        element = my_list[i]
        if all(element > x for x in my_list[i+1:]):
            return element
