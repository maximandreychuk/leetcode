from psycopg2 import connect


def findLengthOfLCIS(nums):
    counter = 1
    result = 0
    for i in range(1, len(nums)):
        if nums[i]>nums[i-1]:
            counter += 1
        else:
            if counter > result:
                result = counter
            counter = 1
    if counter > result:
        return counter
    return counter if result == 0 else result


print(findLengthOfLCIS([1,3,5,4,7])) # 3
print(findLengthOfLCIS([2,2,2,2,2])) # 1
print(findLengthOfLCIS([1,3,5,7])) # 4
print(findLengthOfLCIS([1,3,5,4,2,3,4,5])) # 4