#!/usr/bin/python3
def add_integer(a, b=98):
    """ The function to add two floats or integers

    >>> add_integer(1, 2)
    3
    >>> add_integer(4, "School")
    b must be an integer
    
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
         return (a + b)
