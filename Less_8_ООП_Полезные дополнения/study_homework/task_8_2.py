"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class MyException(Exception):
    def __init__(self, text):
        self.text = text


def main():
    while True:
        dividend = input('Введите делимое или "q" для выхода: ')
        if dividend == 'q':
            break
        divisor = input('Введите делитель или "q" для выхода: ')
        if divisor == 'q':
            break
        try:
            if float(divisor) == 0:
                raise MyException('На ноль делить нельзя!!!!!!11')
            else:
                print(f'Частное: {float(dividend) / float(divisor):.2f}')
        except MyException as ex:
            print(ex)
        except ValueError as ex:
            print(ex)


if __name__ == '__main__':
    main()
