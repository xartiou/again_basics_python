

def log(func):
    """Decorator"""
    def decorated(*args, **kwargs):
        """Wrapper"""
        res = func(*args, **kwargs)
        print(f"log: {func.__name__} ({args}, {kwargs}) = {res}")
        return res
    return decorated

@log
def my_func(val_1, val_2):
    """Простое вычисление"""
    return val_1 + val_2


my_func(14, 15)
