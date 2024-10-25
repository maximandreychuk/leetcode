def canAliceWin(nums):
    al = bob = 0
    for i in nums:
        if i < 10:
            al += i
        else: bob += i
    return al != bob

print(canAliceWin([1,2,3,4,10]))