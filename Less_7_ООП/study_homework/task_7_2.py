"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import abstractmethod


# class Clothes:
#
#     def __init__(self, param):
#         self.param = param
#
#     @abstractmethod
#     def expense(self):
#         """абстр. метод расхода ткани"""
#         pass
#
#     def __str__(self):
#         """преобразует объект к строке"""
#         return str(self.param)
#
#
# class Coat(Clothes):
#
#     @property
#     def expense(self):
#         """Расчет ткани для пальто"""
#         return self.param / 6.5 + 0.5
#
#
# class Costume(Clothes):
#     @property
#     def expense(self):
#         """ """
#         return 2 * self.param + 0.3
#
#
# coat = Coat(180)
# costume = Costume(52)
# print(coat.expense)
# print(costume.expense)


'''-------------------variant----------------------------'''



class Clothes:
    """класс одежда"""
    cloth_all = 0  # общий расход ткани на одежду

    def __init__(self, param):
        self.param = param
        Clothes.summ_on_cloth(self, self.cloth_counting)

    @abstractmethod
    def cloth_counting(self):
        pass

    # Функция подсчитывает сколько всего надо ткани на всю одежду и сохранит в параметр .cloth_al
    def summ_on_cloth(self, result):
        Clothes.cloth_all += result

    def __str__(self):
        return f'Ткани для объекта = {round(self.cloth_counting), 2}. Всего ткани = {round(self.cloth_all), 2}'


class Coat(Clothes):
    # Функция покажет сколько надо ткани непосредственно для пальто
    @property
    def cloth_counting(self):
        try:
            return int(self.param) / 6.5 + 0.5
        except ValueError:
            return f'Неверное значение {self.param}'


class Costume(Clothes):
    # Функция покажет сколько надо ткани непосредственно для костюма
    @property
    def cloth_counting(self):
        try:
            return int(self.param) * 2 + 0.3
        except ValueError:
            print(f'Неверное значение {self.param}')


coat_1 = Coat(58)
print(coat_1)

print('*' * 50)

coat_2 = Coat(40)
print(coat_2)

print('*' * 50)

costume_1 = Costume(190)
print(costume_1)

print('*' * 50)

costume_2 = Costume(180)
print(costume_2)

print('*' * 50)