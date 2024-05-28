# Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
#методы для определения дня недели, проверки на високосный год и определения
#количества дней в месяце
import calendar
from datetime import datetime

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


my_calendar = Calendar()

print("День недели:", my_calendar.weekday())
print("Високосный год:", my_calendar.leap_year())
print("Дни в месяце:", my_calendar.days_in_month())
