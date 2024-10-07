# Напишите программу, которая проверит каждое число в списке на предмет того, является ли оно простым.

def simple(n):
    is_true, is_false = 2, 0
    for i in range(1,n+1):
        if n % i == 0:
            is_false += 1
    return is_false <= is_true


