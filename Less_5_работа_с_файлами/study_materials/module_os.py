"""
Модуль OS
"""
import os

# os.remove("my_file.txt")
# os.rename("test.txt", "pytest.txt")
# os.listdir() Отвечает за получение списка папок и файлов для определённой директории.
content = os.listdir(path=".")
print(content)
content_pre = os.listdir(path="..")
print(content_pre)

# os.path.basename() Возвращает название файла пути
print(os.path.basename(
    r"/home/xartiou/PycharmProjects/again_basics_python/Less_5_работа_с_файлами/study_materials/study_file.py"))
# os.path.dirname() Возвращает часть каталога пути
print(os.path.dirname(r"study_materials/study_file.py"))
# os.path.exists() Проверяет, присутствует ли указанный файл.
print(os.path.exists(
    r"/home/xartiou/PycharmProjects/again_basics_python/Less_5_работа_с_файлами/study_materials/study_file.py"))
# os.path.isdir(), os.path.isfile() Проверяет, является ли объект папкой или файлом.
# os.path.join() Позволяет объединить несколько путей.
# os.path.split() Разделяет путь на кортеж, содержащий и путь до каталога, и имя файла.
print(os.path.split(
    r"/home/xartiou/PycharmProjects/again_basics_python/Less_5_работа_с_файлами/study_materials/study_file.py"))