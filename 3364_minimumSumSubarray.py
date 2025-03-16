def minimumSumSubarray(nums,l,r):
    import math
    result = math.inf
    for i in range(len(nums)-r):
        head = l
        while head < r:
            print(nums[i:head+1], sum(nums[i:head+1]))
            if sum(nums[i:head+1]) < result:
                result = sum(nums[i:head+1])
            head += 1
    return result



#print(minimumSumSubarray(nums = [3, -2, 1, 4], l = 2, r = 3))
print(minimumSumSubarray(nums = [-2, 2, -3, 1], l = 2, r = 3))
#no