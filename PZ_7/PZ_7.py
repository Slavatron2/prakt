#Дано целое положительное число. Вывести символы, изображающие цифры этого
#числа (в порядке справа налево).
def vrm(num):
    digits = str(num)
    for digit in digits[::-1]:
        print(digit)

num = 12345
vrm(num)