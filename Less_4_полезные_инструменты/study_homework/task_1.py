"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


def salary_calculation(hours_worked, rate_per_hour, bonus):
    """
    :param hours_worked: отработано часов
    :param rate_per_hour: ставка за час
    :param bonus: премия
    :return: (hours_worked * rate_per_hour) + bonus
    """
    return (hours_worked * rate_per_hour) + bonus


print(salary_calculation(56, 1200, 5000))

# вариант
from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")


salary()