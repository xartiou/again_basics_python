"""
7. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""


# решение без прошлой функции
# def int_func():
#     my_str = str(input("Введите через пробел слова на латинице: ")).title()
#     return my_str
#
#
# print(int_func())


def int_func(word):
    return word[0].upper() + word[1:].lower()


s = input().split()
for i, word in enumerate(s):
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('error!')
    else:
        s[i] = int_func(word)
print(' '.join(s))
