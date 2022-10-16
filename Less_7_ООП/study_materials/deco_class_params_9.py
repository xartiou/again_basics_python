import time


class Sleep:
    """Класс декоратор"""
    def __init__(self, timeout):
        self.timeout = timeout

    def __call__(self, func):
        def decorated(*args, **kwargs):
            """Wrapper"""
            time.sleep(self.timeout)
            res = func(*args, **kwargs)
            print("Function {} was sleeping in class".format(func.__name__))
            return res
        return decorated


@Sleep(3)
def factorial(param):
    """Calculate factorial"""
    if param <= 1:
        return 1
    else:
        return param * factorial(param - 1)


print(factorial(5))
