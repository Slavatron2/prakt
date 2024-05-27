#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму всех
# элементов списка, кроме элементов с номерами от K до L включительно.#
import random

a = int(input("Введите значение а: "))
b = int(input("Введите значение b: "))
n = int(input("Введите значение n: "))

def vrm(lst, k, l):
    ben = 0
    for i in range(len(lst)):
        if i < k-1 or i > l-1:
            ben += lst[i]
    return ben

k = int(input("Введите значение K: "))
l = int(input("Введите значение L: "))

c = []

for i in range(n):
    numbers = random.randint(a, b)
    c.append(numbers)

print(c)
print(vrm(c, k, l))
