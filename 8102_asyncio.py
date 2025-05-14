# Задача 3: Асинхронный ввод/вывод (I/O) с использованием asyncio.sleep
# Напишите асинхронную функцию download_data(url), которая имитирует загрузку данных из сети. Функция должна:
# 1. Принять URL в качестве аргумента.
# 2. Вывести в консоль сообщение “Начинаем загрузку данных из {url}”.
# 3. Использовать asyncio.sleep для имитации задержки загрузки (например, 2 секунды).
# 4. Вывести в консоль сообщение “Данные из {url} загружены”.
# 5. Вернуть строку “Данные из {url}”.
# Затем напишите главную асинхронную функцию, которая создает список из нескольких URL-адресов и
# параллельно загружает данные из каждого URL-адреса, используя asyncio.gather.
import asyncio

async def download_data(url):
    print(f'Начинаем загрузку данных из {url}')
    await asyncio.sleep(2)
    print(f'Данные из {url} загружены')
    return f'Данные из {url}'

async def main():
    urls = [
        'https://foo.ru',
        'https://gro.ru',
        'https://loo.ru'
    ]
    tasks = [download_data(url) for url in urls]
    for i in await asyncio.gather(*tasks):
        print(i)


# asyncio.run(main())

a = [1,2,3,4]
print(a[:])
print(a[:-1])
