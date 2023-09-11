#!/usr/bin/python3
"""This module contains a code to get a matrix and divisor
"""


def matrix_divided(matrix, div):
    """This function divides a matrix and returns a new matrix
    Args:
        matrx: gets the matrix to be divided
        div: the divisor
    Returns:
        return a new divided matrix
    """
    try:
        new_matrix = []
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        for mat_list in range(len(matrix)):
            new_index_list = []
            if len(matrix[mat_list]) != len(matrix[mat_list-1]):
                raise TypeError("Each row of the matrix must"
                                " have the same size")
            new_matrix.append(new_index_list)
            for element in matrix[mat_list]:
                if not isinstance(element, (int, float)):
                    raise TypeError("matrix must be a matrix "
                                    "(list of lists) of integers/floats")
                mat_div = round(element/div, 2)
                new_index_list.append(mat_div)
        return new_matrix
    except TypeError as var:
        return (var)
    except ZeroDivisionError as e:
        return (e)


if __name__ == "__main__":
    import doctest
    doctest.textfile("tests/2-matrix_divided.txt")
