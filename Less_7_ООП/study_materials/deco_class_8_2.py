import functools


class Log:
    def __init__(self, func):
        """Класс-декоратор"""
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        """Обертка"""
        res = self.func(*args, **kwargs)
        print(f"log: {self.func.__name__}, {self.func.__doc__}: ({args}, {kwargs}) = {res}")
        return res


@Log
def my_func(val_1, val_2):
    """Возведение в степень"""
    return val_1 ** val_2


print("--Функция с декоратором--")
my_func(2, 3)
