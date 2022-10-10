"""
2. Реализовать класс Road (дорога),
в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_asphalt_mass(self):
        return f"Масса асфальта для дороги длиной: {self._length}м. и шириной: {self._width}м.," \
               f" составит: {self._length * self._width * 25 * 5 / 1000} тонн."


r = Road(100, 6)
print(r.calculation_asphalt_mass())

"""
# Вариант решения
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        print(f"Масса асфальта - {self._length * self._width * 25 * 5 / 1000} тонн")


def main():
    while True:
        try:
            road_1 = Road(int(input("Введите ширину дороги в метрах: ")), int(input("Введите длину дороги в метрах: ")))
            road_1.calc()
            break
        except ValueError:
            print("Only integer!")


if __name__ == "__main__":
    main()
"""