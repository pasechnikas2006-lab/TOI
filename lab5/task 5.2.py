import random
import math
import statistics


def analyze_numbers():

    # Генерируем список из 100 случайных чисел от 1 до 100
    numbers = [random.randint(1, 100) for _ in range(100)]

    # Среднее арифметическое
    mean = statistics.mean(numbers)

    # Медиана
    median = statistics.median(numbers)

    # Стандартное отклонение
    stdev = statistics.stdev(numbers)

    # Квадратный корень из суммы всех чисел (округленный)
    sqrt_sum = math.sqrt(sum(numbers))
    rounded_sqrt = round(sqrt_sum, 2)

    # Выводим результаты с округлением до 2 знаков
    print(f"Среднее: {mean:.2f}, Медиана: {median:.1f}, "
          f"Стандартное отклонение: {stdev:.2f}, "
          f"Корень из суммы: {rounded_sqrt:.2f}")
    print(numbers)
    return numbers


analyze_numbers()
