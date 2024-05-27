#Дана строка, состоящая из русских слов, разделенных пробелами (одним или
#несколькими). Вывести строку, содержащую эти же слова, разделенные одним
#символом «.» (точка). В конце строки точку не ставить.

def vrm(cpu):
    SLOVA = cpu.split()
    words = '.'.join(SLOVA)
    return words

words = str(input("Enter text: "))

cpu = vrm(words)
print(cpu)
