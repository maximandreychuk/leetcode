def two_sum(nums, target):
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums) - 1:
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        if nums[i] + nums[-1] == target:
            return [i, j]\
        s = 'svsv'
        for i in s:
            if i.is


print(two_sum(nums = [2,7,11,15], target = 9))
print(two_sum(nums = [3,2,4], target = 6))