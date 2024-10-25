def decompressRLElist(nums):
    res = []
    for i in range(0, len(nums), 2):
        add =[nums[i+1]] * nums[i]
        res += add
    return res



print(decompressRLElist([1,1,2,3])) # [1,3,3]