# Дана строка "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4". Преобразовать информацию из строки в словарь, найти среднее
# арифметическое оценок, результаты вывести на экран.

stroka = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"
grisha = {}
ocenki = []
spiski = stroka.split()
grisha["Фамилия"] = spiski[0]
grisha["Имя"] = spiski[1]
grisha["Группа"] = spiski[2]
for i in spiski[3:11]:
  ocenki.append(int(i))
a = sum(ocenki)/len(ocenki)
grisha["Средний бал"] = a
print(grisha)
