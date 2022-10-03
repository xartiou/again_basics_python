"""
Для использования менеджера контекста применяется оператор with.
Такой механизм выполняет автоматическое закрытие файла после завершения работы с ним.
"""
with open("new_file.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        print(line)


# обработка ошибок при работе с файлами
try:
    with open("new_file.txt", "r", encoding="utf8") as read_file:
        for line in read_file:
            print(line)
except IOError:
    print("Произошла ошибка ввода-вывода!")

