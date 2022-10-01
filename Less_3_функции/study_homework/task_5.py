def my_func():
    """
    Функция запрашивает у пользователя строку чисел, разделенных пробелом.
    При нажатии Enter должна выводиться сумма чисел.
    Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
    Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
    Но если вместо числа вводится специальный символ, выполнение программы завершается.
    Если специальный символ введен после нескольких чисел,
    то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
    :return:
    """
    # сумма введенных чисел
    s = 0
    while True:
        # запрашивает у пользователя строку чисел, разделенных пробелом.
        in_list = input('Введите числа через пробел или Q для выхода: ').upper().split()
        for i in in_list:
            if i == 'Q':
                print(s)
                break
            try:
                s += float(i)
            except ValueError:  # когда в функцию передан аргумент с неподдерживаемым значением.
                print(f'Значение {i} не было учтено при подсчёте суммы - неверный тип')
        else:
            # если символа завершения программы не было, продолжаем ввод
            print(s)
            continue
        # сюда мы дойдём, только если встретим символ завершения программы
        break
    return s


my_func()


# вариант решения без функции
# num = 0
# try:
#     while True:
#         for i in map(int, input('Введите числа через пробел. Для выхода нечисловой символ: ').split()):
#             num += i
#         print(num)
# except ValueError:
#     print(num)
