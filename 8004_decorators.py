from functools import wraps

def my_decorator(func):
    @wraps(func) # Декорируем обёртку
    def wrapper(*args, **kwargs):
        """Это обертка!"""
        print("Вызов декорированной функции")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """Это функция, которая говорит hello"""
    print("Hello!")

print(say_hello.__name__)     # Выведет: say_hello
print(say_hello.__doc__)    # """Это функция, которая говорит hello"""

# то есть wraps(func) копирует метаданные из исходной функции в функцию-обертку(wrapper)?
#
# Да, именно так! Ты совершенно верно понял.
# @wraps(func) (где func - это исходная декорируемая функция) берет метаданные
# (например, __name__, __doc__, __module__ и другие) из func и копирует их в функцию-обёртку (wrapper),
# которую ты создаешь внутри своего декоратора.
#
# Это позволяет функции-обёртке “притвориться” исходной функцией, сохраняя её важные характеристики.
# В итоге, когда ты будешь запрашивать информацию о декорированной функции (например, её имя или документацию),
# ты получишь информацию об исходной функции, а не об обёртке.
