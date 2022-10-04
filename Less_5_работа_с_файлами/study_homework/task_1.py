"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('task_1.txt', 'w', encoding='utf-8') as text_file:
    while True:
        line = input('Введите текст, для выхода Enter: ')
        if not line:
            break
        text_file.write(line + '\n')
        # print(line, file=text_file) # Print в файл
