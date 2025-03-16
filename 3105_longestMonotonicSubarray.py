def helper(subarray, flag):
    cnt = 1
    if flag == '>':
        for i in range(1, len(subarray)):
            if subarray[i] > subarray[i-1]:
                cnt += 1
            else:
                break
    if flag == '<':
        for i in range(1, len(subarray)):
            if subarray[i] < subarray[i-1]:
                cnt += 1
            else:
                break
    return cnt

def longestMonotonicSubarray(nums):
    cnt = 1
    for i in range(1, len(nums)):
        increase = decrease = 0
        if nums[i] > nums[i-1]:
            increase = helper(subarray=nums[i-1:], flag='>',)
        elif nums[i] < nums[i-1]:
            decrease = helper(subarray=nums[i-1:], flag='<',)
        potential = max(increase, decrease)
        if potential >= cnt:
            cnt = potential
    return cnt

print(longestMonotonicSubarray(nums = [3,2,1]))
#done, not optimize
