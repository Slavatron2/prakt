#Из заданной строки отобразить только цифры. Использовать библиотекуstring.
#Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
#481 feet (147 metres) high.

import string

text = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."
chifru = ''.join(filter(lambda char: char in string.digits, text))
print("Цифры в строке:", chifru)
