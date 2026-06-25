def contains_duplicate(nums1):
    counter = {}
    for i in nums1:
        counter.setdefault(i, 0)
        counter[i] += 1
        if counter[i] > 1:
            return i