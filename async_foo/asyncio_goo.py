import asyncio

# Напишите асинхронную функцию, которая запускает множество задач (asyncio.sleep()),
# но не более чем N одновременно. Напечатайте результат выполнения всех задач.

async def foo(n):
    for i in range(n):
        await asyncio.sleep(0)
        print(f"Задача {i}")

async def main():
    await foo(3)

asyncio.run(main())