def sortArrayByParity(nums):
    cnt = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[cnt], nums[i] = nums[i], nums[cnt]
            cnt += 1
    return nums



print(sortArrayByParity(nums = [3,1,2,4])) # 2431
