# Разработать программу с применением пакета tk - Дано трёхзначное число.
# Проверить истинность высказывания : "Все цифры данного числа различны
import tkinter as tk

def check_distinct_digits(number):
    digits = set(str(number))
    return len(digits) == 3

def main():
    # Создаем главное окно
    root = tk.Tk()
    root.title("Проверка различных цифр")

    # Создаем поле ввода для номера
    number_label = tk.Label(root, text="Введите трехзначное число:")
    number_entry = tk.Entry(root)

    # Создаем кнопку для проверки
    check_button = tk.Button(root, text="Проверить", command=lambda: check_number(number_entry.get()))

    # Создаем поле вывода для результата
    result_label = tk.Label(root, text="")

    # Размещаем элементы на окне
    number_label.pack()
    number_entry.pack()
    check_button.pack()
    result_label.pack()

    def check_number(number):
        if not number.isdigit() or len(number) != 3:
            result_label["text"] = "Введите корректное трехзначное число."
        else:
            number = int(number)
            result = check_distinct_digits(number)
            if result:
                result_label["text"] = "Все цифры различны."
            else:
                result_label["text"] = "Не все цифры различны."

    # Запускаем главное окно
    root.mainloop()

if __name__ == "__main__":
    main()
