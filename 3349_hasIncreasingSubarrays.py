def hasIncreasingSubarrays(nums, k):
    for i in range(len(nums)-2*k):
        sub1 = nums[i:i+k]
        sub2 = nums[i+k:i+k*2]
        sort_sub1 = sorted(sub1)
        sort_sub2 = sorted(sub2)
        if sub1 == sort_sub1 and sub2 == sort_sub2:
            return True
    return False


print(hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3))
#partial