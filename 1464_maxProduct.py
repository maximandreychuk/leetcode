def maxProduct(nums):
    max_score = float("-inf")
    i = 0
    start_j = 1
    while i < len(nums)-1:
        for j in range(start_j, len(nums)):
            if (nums[i]-1) * (nums[j]-1) > max_score and i != j:
                max_score = (nums[i]-1) * (nums[j]-1)
        i += 1
        start_j += 1
    return max_score



print(maxProduct( nums = [3,4,5,2])) # 12