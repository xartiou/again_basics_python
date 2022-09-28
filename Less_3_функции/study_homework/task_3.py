"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    """
    my_func() принимает три позиционных аргумента
    :return: сумму наибольших двух аргументов
    """
    return sum(sorted([arg_1, arg_2, arg_3])[1:])


print(my_func(5, 8, 4))


# вариант решения
def sum_max(a, b, c):
    my_list = [a, b, c]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Enter only numbers!'


print(sum_max(6, 9, 5))
