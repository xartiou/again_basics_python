"""
Под интерфейсом в ООП понимается описание поведения объекта, т. е., совокупность публичных
методов объекта, которые могут применяться в других частях программы для взаимодействия с ним.
"""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method_1(self):
        pass

    @abstractmethod
    def my_method_2(self):
        pass


class MyClass(MyAbstractClass):
    def my_method_1(self):
        print("Method my_method_1()")

    def my_method_2(self):
        print("Method my_method_2()")


mc = MyClass()
mc.my_method_1()


"""Интерфейс итерации"""

my_list = [30, 105.6, "text", True]
for el in my_list:
    print(el)

ml = my_list.__iter__()
print(ml)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyNumbers()
my_iter = iter(my_class)
for x in my_iter:
    print(x)


"""Создание собственных объектов-итераторов"""


class Iterator:
    """Объект-итератор"""
    def __init__(self, start=0):
        self.i = start

    # Метод __iter__ должен возвращать объект-итератор
    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


class IterObj:
    """
    Объект, поддерживающий интерфейс итерации (итерируемый объект)
    """
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        # Метод __iter__ должен возвращать объект-итератор
        return Iterator(self.start)


obj = IterObj(start=2)
for el in obj:
    print(el)