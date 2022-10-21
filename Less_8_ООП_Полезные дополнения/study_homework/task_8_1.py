"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:

    def __init__(self, data='21-10-2022'):
        self.data = data

    @classmethod
    def data_go_int(cls, data):
        try:
            int_data = tuple(map(int, data.split('-'))) if len(tuple(map(int, data.split('-')))) == 3 else 'Error'
            if int_data == 'Error':
                raise ValueError
            return int_data
        except ValueError:
            print(f'Некорректный ввод.')

    @staticmethod
    def valid_int_data(data):
        valid_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        try:
            day, month, year = Data.data_go_int(data)
            if year % 400 != 0 and year % 100 != 0:
                if 1 <= day <= valid_month[month]:
                    return True
            elif year % 400 != 0 and year % 4 != 0:
                if 1 <= day <= valid_month[month]:
                    return True
            else:
                if month == 2 and 1 <= day <= 29:
                    return True
                elif 1 <= day <= valid_days[month]:
                    return True
            raise Exception
        except KeyError:
            print(f'Некорректная дата! Неверно введен месяц')
            return False
        except TypeError:
            return False
        except Exception:
            print(f'Некорректная дата! Неверно введен день')
            return False
    
                    
def tests():
    data = Data('01-02-2021')
    assert data.data_go_int(data.data) == (1, 2, 2021)
    assert Data().data_go_int('31-08-1999') == (31, 8, 1999)
    assert Data().data_go_int('89-12-1874-1987') == None
    assert Data.valid_int_data('29-02-2000') == True
    assert Data.valid_int_data('25-07-2016') == True
    assert Data.valid_int_data('31-01-2021') == True
    assert Data.valid_int_data('12-03-1900') == True
    assert Data.valid_int_data('15-13-1954') == False
    assert Data.valid_int_data('89-12-1874') == False
    assert Data.valid_int_data('89-12-1874-1987') == False
    assert Data.valid_int_data('Not-valid-data') == False
    assert data.valid_int_data(data.data) == True
    print('All test complite.')


def main():
    while True:
        data = input('Введите дату в формате дд-мм-гг, "q" для выхода или "t" для тестирования: ')
        if data == 'q':
            break
        elif data == 't':
            tests()
            break
        else:
            data = Data(data)
            print(data.data_go_int(data.data))
            print(data.valid_int_data(data.data))


if __name__ == '__main__':
    main()

