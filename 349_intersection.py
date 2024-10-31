def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1.intersection(set2))


print(intersection([4,9,5,5], [9,4,5,5,9,8,4]))
