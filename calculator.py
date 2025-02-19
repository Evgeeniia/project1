import numpy as np

class Calculator:
    def init(matr, matrix):
        matr.matrix = matrix.get_matrix()

    def calculate(matr):
        return np.mean(matr.matrix, axis=0)
