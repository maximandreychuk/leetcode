
def firstBadVersion(nums, target):
    if nums[0] == target:
        return nums[0]
    if target <= nums[:(len(nums)//2)][-1]:
        return firstBadVersion(nums[:(len(nums)//2)], target)
    else:
        return firstBadVersion(nums[(len(nums)//2):], target)




print(firstBadVersion([1,3,5,6,8,10,12,14,16,19],3))
print(firstBadVersion([1,3,5,6,8,10,12,14,16,19],16))