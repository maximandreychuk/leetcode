import asyncio


async def load_data(url):
    print(f'Запрос выполняется {url}')
    await asyncio.sleep(1)
    print(f'Запрос завершился {url}')

async def get_data(url):
    print(f'Другая задача')
    return url


async def main():
    url = 'http://o.com'
    await asyncio.gather(load_data(url), get_data(url))

asyncio.run(main())

