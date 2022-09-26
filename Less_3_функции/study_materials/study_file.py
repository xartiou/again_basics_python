print('В Python функция — это объект.')


def my_sum(arg_1, arg_2):
    return arg_1 + arg_2


print(my_sum(25, 35))
print(my_sum('Paco ', 'Raban'))


def ext_func(var_1):
    def int_func(var_2):
        return var_1 + var_2

    return int_func


f_obj = ext_func(200)
print(f_obj(300))

#  return со значением
#  расчёт полной площади цилиндра

"""def s_calc():
    r_val = float(input("Укажите радиус цилиндра: "))
    h_val = float(input("Укажите высоту цилиндра: "))
    # площадь боковой поверхности цилиндра:
    s_side = 2 * 3.14 * r_val * h_val
    # площадь одного основания цилиндра:
    s_circle = 3.14 * r_val ** 2
    # полная площадь цилиндра:
    s_full = s_side + 2 * s_circle
    return s_full


s_val = s_calc()
print(f'полная площадь цилиндра: {s_val}')"""

#  return без значения

"""def s_calc():
    try:
        r_val = float(input("Укажите радиус: "))
        h_val = float(input("Укажите высоту: "))
    except ValueError:
        return  # В результате функция возвращает объект типа None.

    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_full


print(f'полная площадь цилиндра: {s_calc()}')
"""

# Возврат набора значений
"""def s_calc():
    try:
        r_val = float(input("Укажите радиус: "))
        h_val = float(input("Укажите высоту: "))
    except ValueError:
        return
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_side, s_full


s_side_val, s_full_val = s_calc()
print(f"Площадь боковой пов-ти цилиндра - {s_side_val}; Полная площадь цилиндра - {s_full_val}")
print(f"Площадь боковой пов-ти цилиндра - {round(s_side_val, 2)}; Полная площадь цилиндра - {round(s_full_val, 2)}")"""

print('Аргументы функций')
print('позиционные параметры')


def first_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3


print(first_func(10, 20, 30))

print('именованные параметры')


def second_func(var_2, var_1, var_3):
    print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_3}")


second_func(var_1=10, var_2=20, var_3=30)


# обязательные параметры
def first_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3


print(first_func(10, 20, 30))


# var_2 и var_3 - необязательные параметры
def second_func(var_1, var_2=20, var_3=30):
    return var_1 + var_2 + var_3


print(second_func(15))


# неопределённое число позиционных параметров
def my_func(*args):
    return args


print(my_func(10, "text_1", 20, "text_2"))


# неопределённое число именованных параметров
def my_func(**kwargs):
    return kwargs


print(my_func(el_1=10, el_2=20, el_3="text"))

# Анонимные функции (lambda)
my_func = lambda p_1, p_2: p_1 + p_2
print(my_func(2, 5))
print(my_func("abra", "kadabra"))
print((lambda p_1, p_2: p_1 + p_2)(2, 5))
print((lambda p_1, p_2: p_1 + p_2)("abra", "kadabra"))

new_func = lambda *args: args
print(new_func(10, 20, 30, 40))

"""
Математические функции
 
abs() Принимает целое число или число с плавающей точкой. Возвращает абсолютное значение числа (по модулю)
round() Принимает число с плавающей точкой. Округляет число до ближайшего целого числа.
        Может принимать число знаков после запятой, до которых необходимо выполнить округление
divmod() Принимает два числа, возвращает также два числа (частное и остаток от деления чисел)
pow() Принимает два числа. Позволяет возвести первое число в указанную степень
max() Принимает итерируемый объект и возвращает самый большой элемент
min() Принимает итерируемый объект и возвращает наименьший элемент
sum() Суммирует элементы последовательности
"""

# Функция range() для многократно выполняемых действий
for el in range(4, 30, 4):
    res = el / 2
    print(f"Результат деления {el} на 2: {int(res)}")

"""
Алгоритм создания функции.
1. Определить название функции.
2. Определить в строках документации назначение функции.
3. Определить информативные имена параметров.
"""


def rectangle_area_calc(length, width):
    """
    Возвращает площадь прямоугольника по длине и ширине
    (number, number) -> number
    >>> rectangle_area_calc(10, 10)
    100
    """
    return length * width
