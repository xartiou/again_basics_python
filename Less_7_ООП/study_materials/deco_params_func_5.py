"""Decorator-function with parametr"""

import time
import requests


def decorator(iters):
    """Outer function passes parametr <iter>"""
    def real_decorator(func):
        """Midle function as decorator"""
        def wrapper(*args, **kwargs):
            """Inner function as wrapper"""
            total_time = 0
            for i in range(iters):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                delta_time = end - start
                total_time += delta_time
                print(f'#{i + 1}: {delta_time:.2f}sec.')
            print(f'Average time: {total_time / iters:.2f}sec.')
        return wrapper
    return real_decorator


@decorator(10)
def get_wp(url):
    """Getting request"""
    requests.get(url)


get_wp('https://google.com')  # decorator(10)(get_wp)('https://google.com')
