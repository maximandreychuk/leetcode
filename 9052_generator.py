# Задача 5: Чтение лог-файла с фильтрацией
# У тебя есть лог-файл, в котором каждая строка содержит информацию о событии.
# Напишите генератор filter_log(log_file, search_string),
# который читает лог-файл и выдает только те строки, которые содержат заданную строку search_string.

def filter_log(file_name, search_string):
    with open(file_name, 'r') as file:
        for line in file:
            if search_string in line:
                yield line

for i in filter_log('test_data/text_file.txt', 'middle'):
    print(i)

