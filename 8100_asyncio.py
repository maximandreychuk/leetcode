# Задача 1: Простая сопрограмма (корутина)
#
# Напишите асинхронную функцию greet(name), которая принимает имя в качестве аргумента и
# печатает приветствие с этим именем (например, “Привет, Alice!”). Затем запустите эту корутину в главном цикле событий.

import asyncio

async def greet(name):
    print(f'hi, {name}')

async def main():
    await asyncio.gather(greet('Alisa'))

asyncio.run(main())
