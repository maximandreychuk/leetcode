from collections import defaultdict

def majorityElement(nums):
    dct = {-1:-1}
    for i in nums:
        if i in dct.keys():
            dct[i] += 1
        else:
            dct[i] = 1
    print(dct)
    return [key for key, value in dct.items() if value > len(nums)/2][0]

# print(majorityElement([3,2,3]))


=