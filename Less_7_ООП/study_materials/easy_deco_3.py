import time
import requests


def timer(func):
    """Это сам декоратор"""
    def wrapper(*args, **kwargs):
        """обёртка"""
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Отправляем запрос на адрес: {args[0]}\n'
              f'Время выполнения: {round(end - start, 2)} секунд.')
        return return_value
    return wrapper


@timer
def get_wp(url):
    """
    Получаем ответ сервера
    200 - запрос успешно обработан
    """
    print('Выполняем расчет.')
    res = requests.get(url)
    return res


get_wp('https://google.com')