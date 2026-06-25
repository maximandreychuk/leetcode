def dominantIndex(nums):
    m1, i1 = min(nums), 0
    for i in range(len(nums)):
        if nums[i] > m1:
            m1 = nums[i]
            i1 = i
    nums[i1] = min(nums)
    m2 = min(nums)
    for i in nums:
        if i > m2:
            m2 = i
    if m1 / m2 >= 2:
        return i1
    return -1

print(dominantIndex([3,6,1,0]))