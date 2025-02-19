import numpy as np

from matrix import Matrix
from calculator import Calculator

# Ввод матрицы размерности n * m
n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

# Ввод элементов матрицы
matrix = []
for i in range(n):
    row = list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split()))
    matrix.append(row)

def main():

    #Матрица
    matrix = Matrix(n, m, data)

    #Среднее арифметическое столбцов
    calculator = Calculator(matrix)
    column = calculator.calculate()

# Вывод 
for i in range(m):
    print(f"Среднее арифметическое {i + 1}: {column[i]}")
