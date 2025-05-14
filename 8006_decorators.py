# Дан код
#
# def greeting(name: str) -> str:
#     return f"Hello, {name}!"
# Необходимо реализовать два декоратора add_tag и add_div,
# так чтобы декоратор add_tag принимал в качестве аргумента тэг
# и оборачивал текст в этот тэг.


def add_tag(tag: str):
    def inner_wrapper(func):
        def outer_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{tag}>{result}<{tag}>'
        return outer_wrapper
    return inner_wrapper

def add_div(func):
    def outer_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<div>{result}<div>'
    return outer_wrapper


@add_tag(tag='h2')
def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting('me'))