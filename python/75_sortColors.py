def sortColors(nums):
    result = [[],[],[]]
    an = []
    for i in nums:
        if i == 0:
            result[0].append(i)
        elif i == 1:
            result[1].append(i)
        else:
            result[2].append(i)
    for _ in result:
        an.extend(_)
    return an



print(sortColors([2,0,2,1,1,0]))

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]