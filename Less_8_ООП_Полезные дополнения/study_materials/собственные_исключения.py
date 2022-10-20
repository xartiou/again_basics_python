"""
Исключение              Описание

Exception               Любое исключение, не являющееся системным
ZeroDivisionError       Попытка деления на ноль
IndexError              Индекс не входит в диапазон элементов
KeyError                Несуществующий ключ
FileExistsError         Попытка создания существующего файла или директории
FileNotFoundError       Файл или директория не существует
IndentationError        Неправильные отступы
TypeError               Несоответствие объекта и типа данных
ValueError              Некорректное значение аргумента функции
"""

"""
print(100/0) 
ZeroDivisionError: division by zero

my_dict = {"k_1": "v_1", "k_2": "v_2", "k_3": "v_3"}
val = my_dict["k_4"]

KeyError: 'k_4'

my_list = [10, 20, 30]
print(my_list[3])

IndexError: list index out of range

В представленных примерах возникают исключения, и выполнение кода завершается с ошибкой. Для
обработки исключений применяются конструкции try/except.
"""

try:
    print(100 / 0)
except:
    print("Деление на ноль недопустимо")

"""В обработке исключений могут быть задействованы инструкции else и finally. Первая выполняется
при отсутствии исключения, вторая — всегда, независимо, было исключение или нет"""

try:
    res = 100 / 10
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(f"Все хорошо. Результат - {res}")
finally:
    print("The end")


"""Создадим собственный класс исключение потомка Exception"""


class MyExcept(Exception):
    def __init__(self, text):
        self.text = text


inp_data = input("Введите положительное число: ")

try:
    inp_data = int(inp_data)
    if inp_data < 0:
        raise MyExcept("Вы ввели отрицательное число!")
except ValueError:
    print("Вы ввели не число")
except MyExcept as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data}")


