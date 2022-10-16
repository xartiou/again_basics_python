"""
специальный механизм, позволяющий использовать метод класса-родителя в
классе-потомке с добавлением некоторой функциональности
"""


class ParentClass:
    def __init__(self):
        print("Konstruktor class_parent")

    def my_method(self):
        print("Method my_method() classa ParentClass")


class ChildClass(ParentClass):
    def __init__(self):
        print("Konstruktor child class")
        # ParentClass.__init__(self)
        # Допустимо также не ссылаться явно на класс-родитель.
        # Для этого используется специальный метод super()
        super().__init__()

    def my_method(self):
        print("Method my_method() class ChildClass")
        # ParentClass.my_method(self)
        # Допустимо также не ссылаться явно на класс-родитель.
        # Для этого используется специальный метод super()
        super().my_method()
        

c = ChildClass()
c.my_method()
