"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divisions(dividend, divisor):
    """
    Функция запрашивает у пользователя два числа и выполняет их деление.
    :return: int(dividend) / int(divisor)
    """
    try:
        return int(dividend) / int(divisor)
    except ZeroDivisionError:
        print('Division by zero is forbidden')
    except ValueError:
        print('You should enter integers')


my_func = (divisions(input("Введите делимое число: "), input("Введите делитель числа: ")))

print(f"Результат деления двух чисел: {round(my_func, 2)}")
