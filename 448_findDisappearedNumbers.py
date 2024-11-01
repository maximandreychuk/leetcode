from collections import defaultdict


def findDisappearedNumbers(nums):
    dct, result = defaultdict(), []
    for i in nums:
        dct[i] = i
    print(dct)
    for i in range(1, len(nums)+1):
        if i not in dct.keys():
            result.append(i)
    return result

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))

