import aiohttp
import asyncio

from aiohttp.abc import HTTPException


# Напишите асинхронную функцию, которая выполняет GET-запрос к указанному URL с помощью aiohttp
# и выводит полученные данные (в формате JSON). Обработайте возможные ошибки.

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, ssl=False) as response:
                # raise HTTPException
                data = await response.json()
                return data
        except Exception as e:
            return print(e)

async def main():
    await fetch_data("https://jsonplaceholder.typicode.com/todos/1")

asyncio.run(main())
