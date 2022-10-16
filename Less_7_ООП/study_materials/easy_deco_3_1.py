import time


def timer(func):
    """Это сам декоратор"""
    def wrapper(*args, **kwargs):
        """обёртка"""
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Расчет функции:  {func.__name__}\n'
              f'Время выполнения: {round(end - start, 2)} секунд.')
        return return_value
    return wrapper


@timer
def get_list_loop(x):
    ll = []
    for idx in range(x):
        ll.append(idx)
    return ll


@timer
def get_list_comp(x):
    return [idx for idx in range(x)]


value = 10 ** 6
get_list_loop(value)
get_list_comp(value)
