"""@staticmethod"""


class Auto:
    @staticmethod
    def get_class_info():
        print("Детальная информация о классе")


Auto.get_class_info()


class SumParam:
    @staticmethod
    def on_sum(param_1, param_2):
        return param_1 + param_2

    def on_sum_1(self, param_1, param_2):
        return SumParam.on_sum(param_1, param_2)


print(f"Вызов статического метода класса: {SumParam.on_sum(25, 20)}")
sp = SumParam()
print(f"Вызов статического метода класса через объект: {sp.on_sum(45, 45)}")

print(f"Вызов статического метода класса через обычный метод класса: {sp.on_sum_1(150, 300)}")


"""@classmethod"""
'''Таким декоратором дополняется метод, который получает класс в качестве первого аргумента.'''


class MyClass:
    @classmethod
    def my_method(cls, param):  # Метод класса
        print(cls, param)


MyClass.my_method(30)  # Вызов метода через название класса
mc = MyClass()
mc.my_method(70)  # Вызов метода класса через экземпляр
