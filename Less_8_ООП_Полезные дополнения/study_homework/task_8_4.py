"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
from abc import ABC, abstractmethod


class ElectronicsWarehouse:
    """Склад электроники"""
    devices_in_warehouse = []

    @classmethod
    def to_warehouse(cls, device):
        cls.devices_in_warehouse.append(device)
        print(device, "Принято на склад.")

    def __str__(self):
        string = '\n'.join(map(str, self.devices_in_warehouse))
        return 'Устройства на складе: \n' + string if string else 'На складе нет устройств'


class ElectronicDevise(ABC):
    """Электроника"""

    def __init__(self, brand, serial, owner='нач. склада'):
        self._brand = brand
        self._serial = serial
        self.owner = owner

    def __str__(self):
        return f'Устройство {self._brand}, номер {self._serial}, ответственный {self.owner}.'

    @abstractmethod
    def func_device(self):
        pass


class Printer(ElectronicDevise):
    def func_device(self):
        print(f'Устройство {self._brand} печатает.')


class Scanner(ElectronicDevise):
    def func_device(self):
        print(f'Устройство {self._brand} сканирует.')


class Copier(ElectronicDevise):
    def func_device(self):
        print(f'Устройство {self._brand} копирует.')


def main():
    printer = Printer('Ricoh', 101)
    scanner = Scanner('HP', 102)
    copier = Copier('Xerox', 103)
    print(printer)
    printer.func_device()
    scanner.func_device()
    copier.func_device()

    print(ElectronicsWarehouse())
    ElectronicsWarehouse.to_warehouse(printer)
    ElectronicsWarehouse.to_warehouse(scanner)
    ElectronicsWarehouse.to_warehouse(copier)
    print(ElectronicsWarehouse())


if __name__ == '__main__':
    main()
