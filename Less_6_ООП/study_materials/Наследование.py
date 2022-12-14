"""
Суть принципа наследования заключается в том, что класс может перенимать (наследовать)
параметры другого класса. Класс, наследующий характеристики другого класса, называется
дочерним, а класс, предоставляющий свои характеристики, — родительским.
"""

# Класс Transport
class Transport:
    def transport_method(self):
        print("Это родительский метод из класса Transport")


# Класс Auto, наследующий Transport
class Auto(Transport):
    def auto_method(self):
            print("Это метод из дочернего класса")


a = Auto()
a.transport_method()  # Вызываем метод родительского класса

