def countPartitions(nums):
    cnt = -1
    for i in range(len(nums)):
        if (sum(nums[:i]) - sum(nums[i:])) % 2 == 0:
            cnt += 1
    return cnt if cnt != -1 else 0

print(countPartitions([10,10,3,7,6]))

#not optimize
