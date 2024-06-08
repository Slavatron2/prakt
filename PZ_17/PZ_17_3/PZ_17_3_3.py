#перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).

import os

os.chdir('../../PZ_11')
shortest_name_file = min((f for f in os.listdir() if os.path.isfile(f)), key=len)
print("Файл с самым коротким именем:", os.path.basename(shortest_name_file))
