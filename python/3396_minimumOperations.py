def minimumOperations(nums):
    cnt = 0
    i = 0
    while True:
        set_nums = set(nums)
        if set_nums == nums:
            return cnt
        i+=3
        if i < len(nums):
            nums = nums[i:]
        else:
            return cnt
        cnt += 1


print(minimumOperations(nums = [1,2,3,4,2,3,3,5,7]))
#partial