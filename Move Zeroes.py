from collections import defaultdict

def moveZeroes(nums):
    zero_idx = 0
    for i in range(0,len(nums)):
        if nums[i] != 0:
            nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
            zero_idx += 1
    return nums






print(moveZeroes(nums = [1,0,0,3,12]))
# print(moveZeroes(nums = [0,1,0,0,3,12]))