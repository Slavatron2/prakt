# В квадратной матрице элементы на главной диагонали увеличить в 2 раза

import random

size = 4
matrix = [[random.randint(0, 10) for _ in range(size)] for _ in range(size)]

print("Исходная матрица:")
for i in matrix:
    print(i)

matrix = [[matrix[i][i] * 2 if i == _ else matrix[i][_] for _ in range(size)] for i in range(size)]

print("Измененная матрица:")
for i in matrix:
    print(i)
