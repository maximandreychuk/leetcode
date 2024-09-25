# Your task is to make a function that can take any non-negative
# integer as an argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
# Input: 42145 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 123456789 Output: 987654321
from sqlalchemy.sql.operators import lshift


def descending_order(num):
    list_num = list(map(int, str(num)))
    sorted_list_num = sorted(list_num)[::-1]
    result = ""
    for i in sorted_list_num:
        result+=str(i)
    return int(result)


print(descending_order(15))