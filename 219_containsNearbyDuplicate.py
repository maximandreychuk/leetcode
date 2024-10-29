def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
    return False

def containsNearbyDuplicate(nums, k):
    seen={}
    for i, num in enumerate(nums):
        if num in seen and abs(i - seen[num]) <= k:
            return True
        seen[num] = i
    return False



print(containsNearbyDuplicate([1,0,1,1], 1)) # true
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # false
print(containsNearbyDuplicate([1,2,3,1], 3))# true