def shuffle(nums, n):
    j = n
    i = 0
    result = []
    while j < len(nums):
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1
    return result




print(shuffle(nums=[2,5,1,3,4,7], n=3))