def findMaxAverage(nums, k):
    head = k
    result = k
    if len(nums) < k:
        return sum(nums) / len(nums)
    for i in range(len(nums)):
        add = sum(nums[i:head + 1])
        if add > result:
            result = add




print(findMaxAverage(nums = [5], k = 4))
print(findMaxAverage(nums = [1, 12, -5, -6, 50, 3], k = 4))

