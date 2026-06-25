# Представь, что у тебя есть очень большой текстовый файл,
# который не помещается в оперативную память целиком.
# Напишите генератор read_large_file(file_path, chunk_size=4096),
# который читает файл по частям (размером chunk_siz байт) и возвращает каждую часть как строку.

def read_large_file(file_path, chunk_size=4096):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read()
            if not chunk:
                break
            yield chunk


for i in read_large_file('test_data/text_file.txt'):
    print(i)
