#.Даны две последовательности. Найти элементы, различные для двух
#последовательностей и их среднее арифметическое.
import random


def amogus(chisla1, chisla2):
    elements = set(chisla1).symmetric_difference(set(chisla2))
    aboba = sum(elements) / len(elements) if len(elements) > 0 else 0
    return list(elements), aboba


chisla1 = [random.randint(0, 10) for _ in range(10)]
chisla2 = [random.randint(0, 10) for _ in range(10)]

elements, aboba = amogus(chisla1, chisla2)
print("Уникальные элементы:", elements)
print("Среднее арифметическое уникальных элементов:", aboba)
