def sortArrayByParityII(nums):
    new_nums = [0 for _ in range(len(nums))]
    cht, ncht = 0, 1
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_nums[cht] = nums[i]
            cht += 2
        else:
            new_nums[ncht] = nums[i]
            ncht += 2
    return new_nums

print(sortArrayByParityII([4,2,5,7])) # [4,5,2,7]