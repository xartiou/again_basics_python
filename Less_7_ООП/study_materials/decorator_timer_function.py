import time


# функция декорирования

def my_timer(func):
    """функция декоратор подсчета времени выполнения функции"""
    def tmp(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        delta_time = time.time() - start_time
        print(f"время выполнения функции: {delta_time}")
        return result
    return tmp


@my_timer
# функция для декорирования
def my_sum(x, y, z):
    return x + y + z


print(my_sum(18569856534642, 963531613842656, 4364131631365131))