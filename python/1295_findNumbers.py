def findNumbers(nums):
    res = 0
    for i in nums:
        if len("".join(str(i))) % 2 == 0: res += 1
    return res


print(findNumbers([12,345,2,6,7896]))
