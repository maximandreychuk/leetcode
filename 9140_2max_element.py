def search2max(nums):
    if len(nums) < 2:
        return -1
    m1, m2 = max(nums[0], nums[1]), min(nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] > m2 and nums[i] > m1:
            m2 = m1
            m1 = nums[i]
        elif nums[i] > m2 and nums[i] < m1:
            m2 = nums[i]
    return m2



print(search2max([2,3,12,32,10,11,20]))
