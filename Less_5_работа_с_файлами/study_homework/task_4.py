"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("task_4.txt", "r", encoding="utf8")as read_file:  # контекстным менеджером читаем файл
    with open('new_task_4.txt', 'w', encoding='utf-8') as new_file:  # контекстным менеджером записываем в новый файл
        for line in read_file:
            eng, *num = line.split()  # разбиваем строку
            ru = translator[eng]  # заменяем на русский
            new_file.write(' '.join([ru] + num) + '\n')  # Запись данных в файл

"""
# Вариант решения
d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('../examples5/text_4.txt', 'r', encoding='utf-8') as f:
    with open('text_4.txt', 'w', encoding='utf-8') as f2:
        f2.writelines([line.replace(line.split()[0], d.get(line.split()[0])) for line in f])
"""

"""
# Вариант решения
with open("examples5\\text_4.txt", 'r') as f, open('text3.txt', 'w', encoding="utf-8") as fil:
    my_dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
    my_str = str()
    for line in f:
        line = line.split()
        for item in my_dict.items():
            if line[0] == item[0]:
                line[0] = item[1]
                my_str = " ".join(line)
                fil.writelines(my_str + '\n')

"""

"""
# Вариант решения
# pip install googletrans==4.0.0-rc1
from googletrans import Translator

with open('text_4.txt', 'w', encoding='utf-8') as f2:
    with open('../examples5/text_4.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    try:
        f2.write(Translator().translate(text, dest='ru').text)
    except AttributeError:
        print('DDOS-атака на Google не прошла')
"""
