#!/usr/bin/python3
"""This modules contains a matrix multiplier
"""


def matrix_mul(m_a, m_b):
    """ This is a function for multiplying matrixes

    Args:
        m_a: This is matrix a
        m_b: This is the matrix b
    Return:
        A new matrix
    """
    try:
        def validate_matrix(matrix):
            """ This checks for the error type

            Args:
                matrix: checks each matrix for error or type
            Return: return the stated error
            """
            if not isinstance(matrix, list):
                raise TypeError("m_a must be a list or m_b must be a list")
            if not all(isinstance(row, list) for row in matrix):
                raise TypeError("m_a must be a list of lists or m_b must"
                                " be a list of lists")
            if not matrix or not all(matrix):
                raise ValueError("m_a can't be empty or m_b can't be"
                                 " empty")
            row_size = len(matrix[0])
            if not all(len(row) == row_size for row in matrix):
                raise TypeError("Each row of m_a must be of the same"
                                " size or each row of m_b must be of the"
                                " same size")
            if not all(isinstance(val, (int, float)) for row in matrix
                       for val in row):
                raise TypeError("m_a should contain only integers or"
                                " floats or m_b should contain only"
                                " integers or floats")

        validate_matrix(m_a)
        validate_matrix(m_b)
        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

        l = []
        for i in range(len(m_a)):
            m = []
            for t in range(len(m_b)):
                f = 0
                for j in range(len(m_a[i])):
                    d = m_a[i][j]*m_b[j][t]
                    f = f+d
                m.append(f)
            l.append(m)
        return l
    except TypeError as a:
        return(a)
    except ValueError as b:
        return(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
