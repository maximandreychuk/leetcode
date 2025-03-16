def selfDividingNumbers(left, right):
    res = nums = []
    for i in range(left, right + 1):
        try:
            for l in str(i):
                i // int(l)
            nums.append(i)
        except ZeroDivisionError:
            pass
    for i in nums:
        li = [int(j) for j in str(i)]
        flag = len(li)
        while flag != 0:
            for n in li:
                if i % n == 0:
                    flag -= 1
            if flag == 0:
                res.append(i)
            flag = 0
    return res




print(selfDividingNumbers(left = 1, right = 22))
# print(selfDividingNumbers(left = 47, right = 85))