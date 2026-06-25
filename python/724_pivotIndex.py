def pivotIndex(nums):
    for i in range(len(nums)):
        if sum(nums[0:i]) == sum(nums[i+1:]):
            return i
    return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([2,1,-1]))