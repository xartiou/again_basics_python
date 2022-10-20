"""
Атрибут         Описание

__name__        Имя класса
__module__      Имя модуля
__dict__        Словарь с атрибутами класса
__bases__       Кортеж с базовыми классами
__doc__         Строка документации класса
__class__       Объект:класс, экземпляром которого является этот инстанс
__init__        Конструктор
__del__         Деструктор
__hash__        Возвращает хеш:значение объекта, равное 32:битному числу
__getattr__     Возвращает атрибут, недоступный обычным способом
__setattr__     Присваивает значение атрибуту
__delattr__     Удаляет атрибут
__call__        Выполняется при вызове экземпляра класса
__str__         Строковое представление объекта
__repr__        Формальное строковое представление объекта
__getitem__     Получение элемента по индексу или ключу
__setitem__     Присваивание элемента с данным ключом или индексом
__delitem__     Удаление элемента с данным ключом или индексом
"""


class User:

    def __init__(self, name, login, password, email):
        self.name = name
        self.login = login
        self.password = password
        self.email = email

    def on_get_data_user(self):
        print(f"Name: {self.name}\n"
              f"Login: {self.login} Password: {self.password}\n"
              f"@mail: {self.email}\n")


usr = User("Ivan", "iii", "12345", "iii@mail.ru")
usr.on_get_data_user()

print(f"__name__ : {User.__name__},\n __module__ : {User.__module__},\n "
      f"__dict__ : {User.__dict__},\n __bases__ : {User.__bases__},\n"
      f"__doc__ : {User.__doc__},\n __class__ : {User.__class__},\n"
      f"__init__ : {User.__init__},\n __hash__ : {User.__hash__}")
