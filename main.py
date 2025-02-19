import numpy as np

# Ввод матрицы размерности n * m
n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

# Ввод элементов матрицы
matrix = []
for i in range(n):
    row = list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split()))
    matrix.append(row)

# Преобразуем список в numpy массив
matrix = np.array(matrix)

# Вычисление среднего арифметического для каждого столбца
column_means = np.mean(matrix, axis=0)

# Вывод результата
for i in range(m):
    print(f"Среднее арифметическое для столбца {i + 1}: {column_means[i]}")
