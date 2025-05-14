# Реализуйте декоратор, который кеширует значение функций на кол-во seconds.
# Если значение взято после выполнения функции нужно вывести в консоль run,
# если же значение взято из кеша, в консоль нужно вывести cache.
import random
import time
from functools import wraps

def cache_for(*, seconds: int):
    cache = {}
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache and time.time() - cache[key]['time'] < seconds:
                print('cache')
                return cache[key]['time']
            else:
                print('run')
                result = func(*args, **kwargs)
                cache[key] = {'result': result, 'time': time.time()}
                return result
        return inner_wrapper
    return outer_wrapper

@cache_for(seconds=2)
def foo():
    return 2

foo()
foo()
time.sleep(2)
foo()

