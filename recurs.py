# Write a function, persistence, that takes in a positive parameter num and
# returns its multiplicative persistence, which is the number of times you must multiply the digits in
# num until you reach a single digit.
#
# For example (Input --> Output):
#
# 39 --> 3 (because 39 = 27, 27 = 14, 14 = 4 and 4 has only one digit, there are 3 multiplications)
# 999 --> 4 (because 999 = 729, 729 = 126, 126 = 12, and finally 12 = 2, there are 4 multiplications)
# 4 --> 0 (because 4 is already a one-digit number, there is no multiplication)

step = 0

def persistence(n):
    global step
    lst = [int(i) for i in str(n)]
    if len(lst) == 1:
        return step // 2
    else:
        res = 1 * lst[0]
        lst = lst[1:]
        step += 1
        while len(lst) != 0:
            res = res * lst[0]
            lst = lst[1:]
        return persistence(res)