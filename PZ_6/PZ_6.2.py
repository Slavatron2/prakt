#Дано множество A из N точек на плоскости и точка B (точки заданы своими
#координатами х, у). Найти точку из множества A, наиболее близкую к точке B.
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по
#формуле:
#R = √(x2 – x1)2 + (у2 – y1)2
#Для хранения данных о каждом наборе точек следует использовать по два списка: первый
#список для хранения абсцисс, второй — для хранения ординат.#
import math

def vrm(A, B):
    min_distance = float('inf')
    amogus = None

    for i in range(len(A)):
        x = A[i]
        y = B[0]
        formula = math.sqrt((x - B[0])**2 + (y - B[0])**2)
        if formula < min_distance:
            min_distance = formula
            amogus = (x, y)

    return amogus

A = [1, 2, 3, 4, 5]
B = [10]

result = vrm(A, B)
print(result)

