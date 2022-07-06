#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat_copy = matrix[:]
    mat = []
    for i in range(0, len(mat_copy)):
        mat.append([])
        for j in mat_copy[i]:
            mat[i].append(j**2)
    return mat
