"""
5. Продолжить работу над первым заданием ElectronicWarehouse.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""

from abc import ABC, abstractmethod


class ElectronicsWarehouse:
    """Склад электроники"""
    devices_in_warehouse = {'Printer': [], 'Scanner': [], 'Copier': []}
    user_devices = {'Printer': [], 'Scanner': [], 'Copier': []}

    @classmethod
    def to_warehouse(cls, *devices, from_user=False):
        if not  from_user:
            for device in devices:
                cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
                print(device, "Принято на склад.")
        else:
            for device in devices:
                cls.user_devices[str(device.__class__.__name__)].append(device)
                cls.devices_in_warehouse[str(device.__class__.__name__)].append(device)
                print(device, "Принято на склад.")


    @classmethod
    def from_warehouse(cls, device):
        cls.devices_in_warehouse[str(device.__class__.__name__)].remove(device)
        cls.user_devices[str(device.__class__.__name__)].append(device)
        print(device, 'Передано со склада.')

    def __str__(self):
        string_warehouse = '\n'.join(map(str, (sum(self.devices_in_warehouse.values(), []))))
        string_warehouse = 'Устройства на складе: \n' + string_warehouse \
            if string_warehouse else 'На складе нет устройств'
        string_user = '\n'.join(map(str, (sum(self.user_devices.values(), []))))
        string_user = 'Устройства у пользователей:\n' + string_user \
            if string_user else 'У пользователей нет устройств'
        return string_warehouse + '\n' + string_user


class ElectronicDevise(ABC):
    """Электроника"""

    def __init__(self, brand, serial, owner='нач. склада'):
        self._brand = brand
        self._serial = serial
        self._owner = owner

    def __str__(self):
        return f'Устройство {self._brand}, номер {self._serial}, ответственный {self._owner}.'

    def change_owner(self, owner='нач. склада'):
        print(f'Устройство {self._brand} переписано с {self._owner} на {owner}')
        self._owner = owner
        if self._owner == 'нач. склада':
            ElectronicsWarehouse.to_warehouse(self, from_user=True)
        else:
            ElectronicsWarehouse.from_warehouse(self)

    @classmethod
    def how_much_devices(cls, device='ALL'):
        if str(device) == 'ALL':
            string_warehouse = {key: len(value) for key, value in ElectronicsWarehouse.devices_in_warehouse.items()}
            string_user = {key: len(value) for key, value in ElectronicsWarehouse.user_devices.items()}
        else:
            string_warehouse = {device: len(ElectronicsWarehouse.devices_in_warehouse[device])}
            string_user = {device: len(ElectronicsWarehouse.user_devices[device])}
            string_warehouse = 'Устройства на складе:\n' + '\n'.join(
                '{}: {}'.format(key, value) for key, value in string_warehouse.items()) + '\nИтого: ' + str(
                sum(string_warehouse.values()))
            string_user = 'Устройства у пользователей:\n' + '\n'.join(
                '{}: {}'.format(key, value) for key, value in string_user.items()) + '\nИтого: ' + str(
                sum(string_user.values()))
            return string_warehouse + '\n' + string_user

    @abstractmethod
    def func_device(self):
        print(f'Устройство {self._brand}, номер {self._serial} находится на складе.')


class Printer(ElectronicDevise):
    def func_device(self):
        if self._owner == 'нач. склада':
            super().func_device()
        else:
            print(f'Устройство {self._brand} печатает.')

    @classmethod
    def how_much_devices(cls, device='Printer'):
        return super().how_much_devices()


class Scanner(ElectronicDevise):
    def func_device(self):
        if self._owner == 'нач. склада':
            super().func_device()
        else:
            print(f'Устройство {self._brand} сканирует.')

    @classmethod
    def how_much_devices(cls, device='Scanner'):
        return super().how_much_devices()


class Copier(ElectronicDevise):
    def func_device(self):
        if self._owner == 'нач. склада':
            super().func_device()
        else:
            print(f'Устройство {self._brand} копирует.')

    @classmethod
    def how_much_devices(cls, device='Copier'):
        return super().how_much_devices()


def main():
    printer = Printer('Ricoh', 101)
    scanner = Scanner('HP', 102)
    copier = Copier('Xerox', 103)
    printer_2 = Printer('Canon', 104)

    print('*'*20)
    copier.func_device()
    print('*'*20)
    ElectronicsWarehouse.to_warehouse(printer, scanner, copier, printer_2)
    print('*' * 20)
    print(ElectronicsWarehouse())
    print('*' * 20)
    printer.change_owner('Inna Vladimirovna')
    print('*' * 20)
    print(ElectronicsWarehouse())
    print('*' * 20)
    copier.change_owner('Donald Duck')
    print('*' * 20)
    copier.func_device()
    print('*' * 20)
    print(ElectronicsWarehouse())
    print('*' * 20)
    printer.change_owner()
    print('*' * 20)
    print(ElectronicsWarehouse())
    print(ElectronicDevise.how_much_devices())
    print('*' * 20)
    print(printer.how_much_devices())


if __name__ == '__main__':
    main()
