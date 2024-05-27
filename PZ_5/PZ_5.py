# Составить функцию, которая выполнит суммирования числового ряда #

a = input("Введите количество чисел, которые хотите просумировать -")
try:
    a = int(a)
    def chislo(n):
        b = 0
        for i in range(1, n+1):
            b += i
        return b
    c = chislo(a)
    print(c)
except:
  print("Ошибка")
