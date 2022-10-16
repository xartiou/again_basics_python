import time


def logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("my_file", 'a', encoding="utf8") as f:
            f.write(
                'Function name: {func_name} with result of the function  = {result}. Start at function{start_time}\n'.
                format(func_name=func.__name__, result=result, start_time=time.ctime(time.time()))
            )
        return result

    return wrapper


@logging
def my_calc(x, y, z):
    return x * y / z


print(my_calc(9, 18, 14))
