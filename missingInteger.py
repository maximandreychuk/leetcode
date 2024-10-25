# Input: nums = [1,2,3,2,5]
# Output: 6
# Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix
#
# [3, 4, 5, 1, 12, 14, 13]. 15
# [3, 4, 6, 1, 12, 14, 13].
from sys import prefix


def foo(nums):
    prefix = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            prefix += nums[i]
        else:
            break
    while prefix in nums:
        prefix += 1
    return prefix



print(foo([3, 4, 5, 1, 12, 14, 13])) # 12 - 15
print(foo([3, 4, 6, 1, 12, 14, 13])) # 7 - 7
print(foo([1, 2, 3, 2, 5])) # 7 - 7
print(foo([1, 2, 3, 2, 5, 4])) # 7 - 7
