"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def mult_list_items(el_1, el_2):
    """
    функция произведения элементов
    :param el_1:
    :param el_2:
    :return:
    """
    return el_1 * el_2


#  формирование списка, используя функцию range() и возможности генератора
my_list = [el for el in range(100, 1001, 2)]
print(reduce(mult_list_items, my_list))

print("*"*20)
# lambda function
print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))

