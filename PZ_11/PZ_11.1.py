#Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме в обратном порядке.


file1 = open("text18-21.txt", encoding="utf-16")
reverse = []
text = []
znaki = 0
for line in file1:
    reverse.append(line)
    text.append(line)
    for i in line:
        if i in "!,.":
            znaki = znaki + 1
print("Количество знаков препинания", znaki)
print("".join(text))
file2 = open("vtoroi_file.txt", "w")
for i in reverse[::-1]:
    stroka = "".join(i)
    file2.write(stroka)




