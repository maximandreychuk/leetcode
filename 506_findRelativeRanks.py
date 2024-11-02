from collections import defaultdict


def findRelativeRanks(nums):
    result, dct, sort = [], defaultdict(), sorted(nums)[::-1]
    for i in range(len(sort)):
        dct[sort[i]] = i
    for i in nums:
        if dct[i] == 0:
            result.append("Gold Medal")
        elif dct[i] == 1:
            result.append("Silver Medal")
        elif dct[i] == 2:
            result.append("Bronze Medal")
        else:
            result.append(str(dct[i]+1))
    return result


print(findRelativeRanks([5,4,3,2,1])) # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(findRelativeRanks([10,3,8,9,4])) # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]