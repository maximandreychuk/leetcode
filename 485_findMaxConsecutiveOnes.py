def findMaxConsecutiveOnes(nums):
    result = 0
    cnt = 0
    for i in nums:
        if i == 1:
            cnt += 1
        else:
            if cnt != 0:
                if cnt > result:
                    result = cnt
            cnt = 0
    if cnt:
        if cnt > result:
            result = cnt
    return result

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
#done