# Задача 2: Параллельное выполнение нескольких корутин
# Напишите две асинхронные функции:
# * print_numbers(): Печатает числа от 1 до 5 с интервалом в 0.5 секунды между каждым числом.
# * print_letters(): Печатает буквы от A до E с интервалом в 0.4 секунды между каждой буквой.
# Используйте asyncio.gather для параллельного выполнения этих двух корутин.
# Пример использования:
import asyncio
from string import ascii_letters as let
let = let[:10]


async def print_numbers(n):
    for i in range(1, n+1):
        await asyncio.sleep(0.5)
        print(i)

async def print_letters(letters):
    for i in range(len(letters)):
        await asyncio.sleep(0.4)
        print(letters[i])

async def main():
    await asyncio.gather(print_numbers(15), print_letters(let))

asyncio.run(main())
