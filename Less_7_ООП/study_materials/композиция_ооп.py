"""
Еще одна особенность ООП — композиция (агрегирование),
когда в классе реализуются вызовы других классов.
Далее при создании экземпляра класса-агрегатора генерируются объекты других классов,
которые являются элементами агрегатора.
"""


class WindowDoor:
    """окна или двери"""
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height


class Room:
    """комната"""
    def __init__(self, len_1, len_2, height):
        """площадь стен комнаты"""
        self.square = 2 * height * (len_1 + len_2)
        """площадь окон и дверей"""
        self.wd = []

    def add_win_door(self, wd_len, wd_height):
        """добавляем площадь окна или двери"""
        self.wd.append(WindowDoor(wd_len, wd_height))

    def common_square(self):
        """вычисляем площадь стен"""
        main_square = self.square
        for el in self.wd:
            """вычитаем из площади стен площади окон и дверей"""
            main_square -= el.square

        return main_square


r = Room(7, 4, 2.5)
print(r.square)  # общая площадь стен
r.add_win_door(1, 2)  # площадь двери(1х2)
r.add_win_door(2.3, 1.2)  # площадь окна(2.3х1.2)
print(r.common_square())  # площадь стен без окон и дверей
