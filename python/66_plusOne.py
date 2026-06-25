def plusOne(digits):
    res = int("".join([str(i) for i in digits]))+1
    return [int(i) for i in str(res)]

print(plusOne([1,2,4]))


