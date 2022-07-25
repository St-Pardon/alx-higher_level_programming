#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function divides the provided matrix with the div param"""

    result = []
    if not div or (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")

        result.append([])

        for j in matrix[i]:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result[i].append(round(j / div, 2))

    return(result)
