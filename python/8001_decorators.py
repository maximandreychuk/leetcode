import logging


logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def handle_exceptions(default_value):
    def wrapper_outer(func):
        def wrapper_inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception:
                return default_value
            return result
        return wrapper_inner
    return wrapper_outer

@handle_exceptions(default_value=['base_data'])
def get_data_from_api(url):
    # Имитация API запроса, который может упасть
    import random
    if random.randint(0, 1) == 0:
        raise ConnectionError("Ошибка соединения с API")
    else:
        return ["data1", "data2", "data3"]

# Задача: Напишите декоратор handle_exceptions, который перехватывает исключения,
# возникающие при выполнении декорируемой функции,
# логирует их и возвращает значение по умолчанию (например, None).

print(get_data_from_api(url='/'))

