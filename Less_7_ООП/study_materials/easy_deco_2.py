import time
import requests


def timer(func):
    """Это сам декоратор"""
    def wrapper():
        """обёртка"""
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения исходной функции: {round(end - start, 2)} секунд.')
    return wrapper


@timer
def get_wp():
    """
    Получаем ответ сервера
    200 - запрос успешно обработан
    """
    print('Выполняем расчет.')
    res = requests.get('https://google.com')
    return res


get_wp()
