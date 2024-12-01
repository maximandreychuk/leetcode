def runningSum(nums):
    result = [nums[0]]
    i = 1
    while i < len(nums):
        result.append(result[i-1]+nums[i])
        i += 1
    return result



print(runningSum(nums = [1,2,3,4])) # [1,3,6,10]