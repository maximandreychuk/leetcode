def maximumProduct(nums):
    max = [nums[2], nums[1], nums[0]]
    for i in range(3, len(nums)):
        if nums[i] > max[0]:
            max[2]=max[1]
            max[1]=max[0]
            max[0] = nums[i]
        elif nums[i] < max[0] and nums[i] > max[1]:
            max[2]=max[1]
            max[1] = nums[i]
        elif nums[i] < max[1] and nums[i] > max[2]:
            max[2] = nums[i]
    return max[0]*max[1]*max[2]





print(maximumProduct([1,2,3,4]))
