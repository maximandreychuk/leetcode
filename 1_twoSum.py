def twoSum(nums, target):
    for i in range(1, len(nums)):
        cnt = i
        while cnt != len(nums):
            if nums[i-1] + nums[cnt] == target:
                return [i-1, cnt]
            cnt += 1

print(twoSum([2,5,5,11], 10))