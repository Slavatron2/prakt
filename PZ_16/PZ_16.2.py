#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате
import calendar
from datetime import datetime
import pickle

class Calendar:
    def __init__(self):
        self.date_time = datetime.now()
    def weekday(self):
        days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        return days_of_week[self.date_time.weekday()]

    def leap_year(self):
        return calendar.isleap(self.date_time.year)

    def days_in_month(self):
        return calendar.monthrange(self.date_time.year, self.date_time.month)[1]


def save_def(calendar_objects, filename):
    """Сохраняет экземпляры класса Calendar в файл"""
    with open(filename, "wb") as f:
        pickle.dump(calendar_objects, f)

def load_def(filename):
    """Загружает экземпляры класса Calendar из файла"""
    with open(filename, "rb") as f:
        calendar_objects = pickle.load(f)
    return calendar_objects

calendar1 = Calendar()
calendar2 = Calendar()
calendar3 = Calendar()
save_def([calendar1, calendar2, calendar3], "calendar.data")

for i in load_def("calendar.data"):
    print(i.weekday())
