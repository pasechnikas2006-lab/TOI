import random
import datetime
from array import array
from datetime import timedelta


def generate_random_dates_with_array():
    # Текущая дата
    end_date = datetime.datetime.now().date()
    # Дата 5 лет назад
    start_date = end_date - timedelta(days=5 * 365)

    # Создаем массив для хранения дней (как целых чисел)
    days_array = array('i')

    # Генерируем 10 случайных дней
    for _ in range(10):
        random_days = random.randint(0, (end_date - start_date).days)
        days_array.append(random_days)

    # Преобразуем дни в даты
    dates = [start_date + timedelta(days=days) for days in days_array]

    # Вычисляем разницу между каждой парой соседних дат
    for i in range(len(dates) - 1):
        diff = abs((dates[i + 1] - dates[i]).days)
        print(f"Разница между {dates[i]} и {dates[i + 1]}: {diff} дней")
    return dates

generate_random_dates_with_array()
