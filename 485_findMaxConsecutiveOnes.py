def findMaxConsecutiveOnes(nums):
    counter = result = 0
    for i in nums:
        if i == 1:
            counter+=1
        else:
            if counter > result:
                result = counter
                counter = 0
    if counter > result:
        return counter
    return result

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
