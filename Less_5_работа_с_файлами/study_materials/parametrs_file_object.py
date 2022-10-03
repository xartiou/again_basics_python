"""
Атрибут         Описание

file.closed     Возвращает значение True, если файл закрыт
file.mode       Возвращает режим доступа, по которому был открыт файл
file.name       Возвращает имя файла

"""

f_obj = open("new_f.txt", "w")
print("Файл. Имя: ", f_obj.name)
print("Файл. Закрыт: ", f_obj.closed)
print("Файл. Режим: ", f_obj.mode)
f_obj.close()
print("Файл. Закрыт: ", f_obj.closed)
f_obj = open("new_f.txt", "w")
new_f_obj = f_obj.write("учиться, учиться и ещё раз учиться")
f_obj.close()
with open("new_f.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        print(line)

# Print в файл
with open("new_f.txt", "a", encoding="utf8") as f_obj:
    print("\nДозаписываем данные в файл при помощи функции print", file=f_obj)

with open("new_f.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        print(line)
        