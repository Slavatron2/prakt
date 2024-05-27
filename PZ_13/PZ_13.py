#В матрице найти минимальный элемент в последней строке

import random

matrix = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
print(" Исходная Матрица:")
for i in matrix:
    print(i)

stroka = matrix[-1]
min_element = min(stroka)

print("Минимальный элемент в последней строке матрицы:", min_element)

