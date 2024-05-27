#В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
#фразу «Министерства образования Ростовской области», посчитать количество
#произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
#«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

with open('hotline.txt', 'r') as file:
    lines = file.readlines()

additions_count = 0
phones_03 = []
phones_50 = []
phones_ege_gia = []

for num, line in enumerate(lines, start=0):
    if "Горячая линия" in line:
        lines[num] = lines[num].replace("Горячая линия", "Горячая линия Министерства образования Ростовской области")
        additions_count += 1
    phone_number = line.split("-")[-1].strip()
    if phone_number.endswith("03"):
        phones_03.append(phone_number)
    elif phone_number.endswith("50"):
        phones_50.append(phone_number)

    if "ЕГЭ" in line or "ГИА" in line:
        phones_ege_gia.append(phone_number)

with open("hotline.txt", 'w', encoding="utf-8") as file:
    txt = "".join(lines)
    file.write(txt)

print(f"Количество добавлений фразы: {additions_count}")
print(f"Номера телефонов, заканчивающиеся на '03': {phones_03}")
print(f"Номера телефонов, заканчивающиеся на '50': {phones_50}")
print("Номера телефонов горячих линий, связанных с ЕГЭ/ГИА:", phones_ege_gia)
