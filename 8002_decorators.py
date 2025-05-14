import logging
import time

logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def cache_result(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
        return result
    return wrapper


@cache_result
def expensive_function(x, y, z=10):
    print("Выполняем тяжелые вычисления...")
    time.sleep(2)  # Имитация долгой работы
    return x * y + z

print(expensive_function(2, 3))
print(expensive_function(2, 3))  # Должно вернуть закешированный результат
print(expensive_function(2, 3, z=20)) # Должно выполнить функцию повторно