import asyncio

# Напишите асинхронную функцию, которая запускает две другие асинхронные функции одновременно.
# Каждая из этих функций имитирует какую-то долгую операцию с помощью asyncio.sleep().
# Функция должна вывести “Завершено” после того, как обе подфункции завершат работу.

async def foo():
    await asyncio.sleep(1)

async def bar():
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(foo(), bar())
    return print("Завершено")

if __name__ == "__main__":
    asyncio.run(main())



