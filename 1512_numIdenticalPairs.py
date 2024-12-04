def numIdenticalPairs(nums):
    i = cnt = 0
    while i < len(nums):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i < j:
                cnt += 1
        i += 1
    return cnt


print(numIdenticalPairs([1,2,3,1,1,3])) # 4