"""
2. Создать текстовый файл (не программно),
    -сохранить в нем несколько строк,
    -выполнить подсчет количества строк,
    -количества слов в каждой строке.
"""
text_file = open("text_file_2.txt", "w", encoding="utf8")

text_line = [
    'Создать текстовый файл\n',
    'сохранить в нем несколько строк\n',
    'выполнить подсчет количества строк\n',
    'количества слов в каждой строке\n'
]
# при помощи метода writelines() запишем строки в файл
text_file.writelines(text_line)
text_file.close()

with open("text_file_2.txt", "r", encoding="utf8") as my_file:
    my_line = my_file.readlines()  # Считывает из файла все строки в список и возвращает его.
    for index, value in enumerate(my_line, 1):
        count_word = len(value.split())
        print(f"Строка {index} содержит {count_word} слов.")
