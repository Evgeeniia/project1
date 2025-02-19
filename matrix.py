import numpy as np

class Matrix:
    def __init__(matr, n, m, data):
        matr.n = n
        matr.m = m
        matr.matrix = np.array(data)

    def get_matrix(matr):
        return matr.matrix
