"""Простейший декоратор-класс"""


class Log:
    """Класс-декоратор"""
    def __call__(self, func):
        def decorated(*args, **kwargs):
            """Обертка"""
            res = func(*args, **kwargs)
            print(f"log: {func.__name__} ({args}, {kwargs}) = {res}")
            return res

        return decorated


@Log()
def my_func(val_1, val_2):
    """Простое вычисление"""
    return val_1 ** val_2


my_func(4, 5)  # Log()(my_func)(4, 5)
