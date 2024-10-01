# Create a function that takes a positive integer
# and returns the next bigger number that can be
# formed by rearranging its digits. For example:
#
#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
from itertools import permutations

def next_bigger(n):
    numbers_list = [int(i) for i in str(n)]
    all_permutations_numbers_list = []
    permutations_list = list(permutations(numbers_list))
    for tup in permutations_list:
        num = int("".join(map(str, tup)))
        all_permutations_numbers_list.append(num)
    next_n = max(all_permutations_numbers_list)
    if next_n <= n:
        return -1
    for numb in all_permutations_numbers_list:
        if numb > n and numb < next_n:
            next_n = numb
    return next_n



print(next_bigger(111))
print(next_bigger(12))
print(next_bigger(21))
# int("".join([str(i) for i in numbers_list]))
