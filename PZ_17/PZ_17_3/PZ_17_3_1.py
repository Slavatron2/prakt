#перейдите в каталог PZ_11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно.

import os

os.chdir("../../PZ_11")
files_in_pz11 = [f for f in os.listdir() if os.path.isfile(f)]
print("Список файлов в каталоге PZ_11:", files_in_pz11)
