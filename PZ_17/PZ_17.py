#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу Вариант(21)

import tkinter as tk
from tkinter import ttk

def submit():
    # Здесь можно добавить логику для обработки введенных данных
    print("Данные подтверждены")

def cancel():
    # Здесь можно добавить логику для отмены ввода
    print("Отмена ввода")

root = tk.Tk()
root.title("Обработка формы")

# Метки и поля ввода
tk.Label(root, text="Форма регистрации пользователя", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Ваше имя:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Пароль:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Возраст:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Пол:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Мужской", variable=gender_var, value="Мужской").grid(row=4, column=1, sticky="w")
tk.Radiobutton(root, text="Женский", variable=gender_var, value="Женский").grid(row=4, column=1)

tk.Label(root, text="Ваши увлечения:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
hobbies_music = tk.BooleanVar()
hobbies_video = tk.BooleanVar()
hobbies_drawing = tk.BooleanVar()
tk.Checkbutton(root, text="Музыка", variable=hobbies_music).grid(row=5, column=1, sticky="w")
tk.Checkbutton(root, text="Видео", variable=hobbies_video).grid(row=5, column=1)
tk.Checkbutton(root, text="Рисование", variable=hobbies_drawing).grid(row=5, column=1, sticky="e")

tk.Label(root, text="Ваша страна:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
country_var = tk.StringVar()
country_combobox = ttk.Combobox(root, textvariable=country_var)
country_combobox['values'] = ("Россия", "Украина", "Беларусь", "Казахстан", "Другие")
country_combobox.grid(row=6, column=1, padx=5, pady=5)

tk.Label(root, text="Ваш город:").grid(row=7, column=0, sticky="e", padx=5, pady=5)
city_var = tk.StringVar()
city_combobox = ttk.Combobox(root, textvariable=city_var)
city_combobox['values'] = ("Москва", "Санкт-Петербург", "Киев", "Минск", "Алматы", "Другие")
city_combobox.grid(row=7, column=1, padx=5, pady=5)

tk.Label(root, text="Кратко о себе:").grid(row=8, column=0, sticky="e", padx=5, pady=5)
entry_about = tk.Text(root, height=4, width=30)
entry_about.grid(row=8, column=1, padx=5, pady=5)

tk.Label(root, text="Решите пример, запишите результат в поле ниже:").grid(row=9, column=0, columnspan=2, padx=5, pady=5)
entry_captcha = tk.Entry(root)
entry_captcha.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

# Кнопки
cancel_button = tk.Button(root, text="Отменить ввод", command=cancel)
cancel_button.grid(row=11, column=0, pady=10)

submit_button = tk.Button(root, text="Данные подтверждаю", command=submit)
submit_button.grid(row=11, column=1, pady=10)

root.mainloop()
