def findDuplicate(nums):
    counter = {}
    for i in nums:
        counter[i] = counter.get(i, 0) + 1
        if counter[i] > 1:
            return i
    return None


print(findDuplicate([1,3,4,2,2]))
# Input: nums = [1,3,4,2,2]
# Output: 2