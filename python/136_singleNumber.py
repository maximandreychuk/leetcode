from collections import defaultdict

def singleNumber(nums):
    dct = {0:0}
    for i in nums:
        if i in dct.keys():
            dct[i] += 1
        else:
            dct[i] = 1
    return [key for key, value in dct.items() if value == 1][0]


print(singleNumber([4,1,2,1,2]))
print(singleNumber([2,2,1]))