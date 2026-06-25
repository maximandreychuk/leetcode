def missingNumber(nums):
    nums = sorted(nums)
    if nums[0] != 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] != 1:
            return nums[i]-1
    return nums[-1]+1



print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))