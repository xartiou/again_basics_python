"""
Механизм наследования может быть реализован с использованием нескольких родителей у одного
класса. И наоборот, один класс-родитель будет передавать свои характеристики нескольким дочерним
классам.
"""


# класс Transport
class Transport:
    def transport_method(self):
        print("Родительский метод класса Transport")


# класс Auto, наследующий Transport
class Auto(Transport):
    def auto_method(self):
        print("Дочерний метод класса Auto")


# класс Bus, наследующий Transport
class Bus(Transport):
    def bus_method(self):
        print("Дочерний метод класса Bus")


a = Auto()
a.transport_method()
a.auto_method()
b = Bus()
b.transport_method()
b.bus_method()


"""
Рассмотрим ещё один пример, в котором класс-родитель Shape определяет атрибуты. Эти атрибуты
могут быть характерны для всех классов-наследников. Например, цвет фигуры, ширина и высота,
основание и высота.
"""


class Shape:
    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)  # возможность работы с атрибутами класса-родителя
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p


class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p


r = Rectangle("white", 10, 20, True)
print(r.color)
print(r.square())
print(r.get_r_p())
t = Triangle("red", 30, 40, False)
print(t.color)
print(t.square())
print(t.get_t_p())


"""
Несколько родителей у одного класса
"""


class Player:
    def player_method(self):
        print("Родительский метод класса Player")


class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Navigator")


class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")


m_p = MobilePhone()
m_p.player_method()
m_p.navigator_method()