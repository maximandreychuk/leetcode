def smallerNumbersThanCurrent(nums):
    i = cnt = 0
    result = []
    while i < len(nums):
        for j in range(len(nums)):
            if i != j:
                if nums[i] > nums[j]:
                    cnt += 1
        result.append(cnt)
        cnt = 0
        i += 1
    return result

print(smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]
