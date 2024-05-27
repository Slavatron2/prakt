import sqlite3


def create_table():
    with sqlite3.connect('OB.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS OB (
                            FIO TEXT,
                            WORK TEXT,
                            SALARY TEXT,
                            TERM TEXT
                        );
                    ''')
        conn.commit()
        print("Таблица создана!")


def add_task(FIO, WORK, SALARY, TERM):
    with sqlite3.connect('OB.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO OB (FIO, WORK, SALARY, TERM)
                      VALUES (?, ?, ?, ?)''', (FIO, WORK, SALARY, TERM))
        conn.commit()


def update_task(FIO, SALARY):
    with sqlite3.connect('OB.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''UPDATE OB SET SALARY = ? WHERE FIO = ?''',
                       (SALARY, FIO))
        conn.commit()


def delete_task(FIO):
    with sqlite3.connect('OB.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM OB WHERE FIO = ?''', (FIO,))
        conn.commit()


def show_tasks():
     with sqlite3.connect('OB.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM OB')
        rows = cursor.fetchall()
        for row in rows:
            print(row)


def delete_all():
     with sqlite3.connect('OB.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM OB """)
        conn.commit()


create_table()

delete_all()
add_task("Manakova Olga Petrovna", "Programming basics teacher", 60000, "31.05.2024")

update_task("Manakova Olga Petrovna", 65000)

delete_task("Manakova Olga Petrovna")

show_tasks()

for i in range(1):
    add_task(f"Манакова Ольга Петровна", "Учитель основ программирования", 70000 + i * 1000, "31.05.2024")
    add_task(f"Мельникова Мария Вячеславовна", "Учитель математики", 35000 + i * 1000, "31.05.2024")
    add_task(f"Кайханиди Виктор Викторович", "Связист", 45000 + i * 1000, "31.05.2024")
    add_task(f"Пивнева Мария Алексеевна", "Основы проектирования БД", 55000 + i * 1000, "31.05.2024")
    add_task(f"Швачич Дмитрий Сергеевич", "Учитель физкультуры", 30000 + i * 1000, "31.05.2024")
    add_task(f"Григорьева Лидия Филиповна", "Продавец бананов", 15000 + i * 1000, "31.05.2024")
    add_task(f"Пильгун Ирина Сергеевна", "Учитель истории", 40000 + i * 1000, "31.05.2024")
    add_task(f"Трищук Софья Артёмовна", "Архитектура аппаратных средств", 40000 + i * 1000, "31.05.2024")
    add_task(f"Прыгунова Татьяна Александровна", "Учитель иностранного языка", 45000 + i * 1000, "31.05.2024")
    add_task(f"Лебедева Мария Викторовна", "Учитель иностранного языка", 45000 + i * 1000, "31.05.2024")
    print(f"Добавлен Учитель основ программирования")
    print(f"Добавлен Учитель математики")
    print(f"Добавлен Связист")
    print(f"Добавлен Учитель Основ проектирования БД")
    print(f"Добавлен Учитель физкультуры")
    print(f"Добавлен Продавец бананов")
    print(f"Добавлен Учитель истории")
    print(f"Добавлен Учитель Архитектуры аппаратных средств")
    print(f"Добавлен Учитель иностранного языка")
    print(f"Добавлен Учитель иностранного языка")
show_tasks()

for i in range(1):
    update_task(f"Манакова Ольга Петровна", 75000 + i * 1000)
    update_task(f"Мельникова Мария Вячеславовна", 40000 + i * 1000)
    update_task(f"Кайханиди Виктор Викторович", 50000 + i * 1000)
    update_task(f"Пивнева Мария Алексеевна", 60000 + i * 1000)
    update_task(f"Швачич Дмитрий Сергеевич", 40000 + i * 1000)
    update_task(f"Григорьева Лидия Филиповна", 17000 + i * 1000)
    update_task(f"Пильгун Ирина Сергеевна", 45000 + i * 1000)
    update_task(f"Трищук Софья Артёмовна", 45000 + i * 1000)
    update_task(f"Прыгунова Татьяна Александровна", 50000 + i * 1000)
    update_task(f"Лебедева Мария Викторовна", 50000 + i * 1000)
    print(f"Обновлен Учитель основ программирования")
    print(f"Обновлен Учитель математики")
    print(f"Обновлен Связист")
    print(f"Обновлен Учитель Основ проектирования БД")
    print(f"Обновлен Учитель физкультуры")
    print(f"Обновлен Продавец бананов")
    print(f"Обновлен Учитель истории")
    print(f"Обновлен Учитель Архитектуры аппаратных средств")
    print(f"Обновлен Учитель иностранного языка")
    print(f"Обновлен Учитель иностранного языка")

show_tasks()
for i in range(1):
    for i in range(1):
        delete_task(f"Манакова Ольга Петровна")
        delete_task(f"Мельникова Мария Вячеславовна")
        delete_task(f"Кайханиди Виктор Викторович")
        delete_task(f"Пивнева Мария Алексеевна")
        delete_task(f"Швачич Дмитрий Сергеевич")
        delete_task(f"Григорьева Лидия Филиповна")
        delete_task(f"Пильгун Ирина Сергеевна")
        delete_task(f"Трищук Софья Артёмовна")
        delete_task(f"Прыгунова Татьяна Александровна")
        delete_task(f"Лебедева Мария Викторовна")

        print(f"Удален Учитель основ программирования")
        print(f"Удален Учитель математики")
        print(f"Удален Связист")
        print(f"Удален Учитель Основ проектирования БД")
        print(f"Удален Учитель физкультуры")
        print(f"Удален Продавец бананов")
        print(f"Удален Учитель истории")
        print(f"Удален Учитель Архитектуры аппаратных средств")
        print(f"Удален Учитель иностранного языка")
        print(f"Удален Учитель иностранного языка")

    show_tasks()
