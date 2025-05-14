def foo(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1



print(foo([1,2,3,4,5,6,7,8,9,10,11,12,13], 12))