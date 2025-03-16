def countSubarrays(nums):
    cnt = 0
    for i in range(len(nums)-2):
        subarray = nums[i:i+3]
        if subarray[0] + subarray[2] == subarray[1] // 2:
            cnt += 1

    return cnt

print(countSubarrays([1,2,1,4,1]))
#partial