from collections import defaultdict

def containsDuplicate(nums):
    dct = defaultdict()
    for i in nums:
        if i in dct.keys():
            return True
        else:
            dct[i] = 1
    return False



print(containsDuplicate([1,2,3,1]))