"""
Перед началом работы с файлом необходимо выполнить процедуру его открытия.
Для этого применяется встроенная функция open().
"""

open_file = open("my_file.txt", "r")

"""
Метод read()
Позволяет прочитать файл целиком
"""
my_file = open("my_file.txt", "r")
content_my_file = my_file.read()
print(content_my_file)
"""
Необходимо всегда выполнять закрытие файла, т. к. другой программе может потребоваться получить
доступ к нему.
"""
open_file.close()
my_file.close()


"""
Метод readline()
Позволяет извлечь очередную строку.
В этом случае извлекается и выводится только первая строка файла. Чтобы извлечь и вывести
остальные, важно выполнить инструкцию столько раз, сколько строк в файле.
"""
my_file = open("my_file.txt", "r")
content_my_file = my_file.readline()
print(content_my_file)
my_file.close()


"""
Метод readlines()
Позволяет извлечь и вывести полный список строк файла.
"""
my_file = open("my_file.txt", "r")
content_my_file = my_file.readlines()
print(content_my_file)
my_file.close()


"""
Чтение файла по частям
Для этого можно использовать построчное извлечение информации из файла с помощью цикла.
"""
my_file = open("my_file.txt", "r")
for line in my_file:
    print(line)
my_file.close()


my_file = open("my_file.txt", "r")
while True:
    content_my_file = my_file.read(1024)
    # содержимое файла извлекается не более килобайта информации или 1024 байтов (символов).
    print(content_my_file)
    if not content_my_file:
        break
my_file.close()

"""
Чтение бинарных (двоичных) файлов
файл открывается в режиме rb (read-binary).
"""
my_file = open("Методичка. Урок 5.pdf", "rb")


"""
Запись данных в файл
"""
wr_file = open("new_file.txt", "w", encoding="utf8")
new_wr_file = wr_file.write("села муха на варенье, вот и всё cтихотворенье.")
wr_file.close()

#  также допустимо применение метода writelines(), принимающего список строк.
wr_file = open("new_file.txt", "w", encoding="utf8")
str_list = ["stroka_1\n", "stroka_2\n", "stroka_3\n"]
wr_file.writelines(str_list)
wr_file.close()



"""
Режимы доступа к файлу.
Режим  Описание
r      Открыть файл на чтение (режим по умолчанию)
w      Открыть на запись. При этом удалить содержимое файла. Если файла нет, создать новый.
x      Открыть файл на запись, если его нет. Если файл есть, он не будет создан.
a      Открыть файл на дозапись. Добавить информацию в конец файла.
b      Открыть файл в двоичном формате.
t      Открыть файл в текстовом формате (режим по умолчанию)
+      Открыть файл на чтение и запись
"""