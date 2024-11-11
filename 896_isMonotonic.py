def isMonotonic(nums):
    flag, i = 0, 1

    while i < len(nums):
        if nums[i] > nums[0]:
            flag = 2
            break
        elif nums[i] < nums[0]:
            flag = 1
            break
        i += 1

    if flag == 0:
        return False

    if flag == 1:
        for i in range(i, len(nums)):
            if nums[i-1] - nums[i] not in [0,1]:
                    return False
    elif flag == 2:
        while i < len(nums):
            if nums[i] - nums[i-1] not in [0,1]:
                return False
            i += 1
    return True


print(isMonotonic(nums = [6,5,4,4]))
print(isMonotonic(nums = [1,2,2,3]))
print(isMonotonic(nums = [2,2,2,2]))


