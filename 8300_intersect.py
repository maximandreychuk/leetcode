def intersect(nums1, nums2):
    if len(nums1) >= len(nums2):
        counter2 = {}
        result = []
        for i in nums1:
            counter2.setdefault(i, 0)
            counter2[i] += 1
        for i in nums2:
            if i in counter2 and counter2[i] > 0:
                result.append(i)
                counter2[i] -= 1
        return result
    else:
        counter2 = {}
        result = []
        for i in nums2:
            counter2.setdefault(i, 0)
            counter2[i] += 1
        for i in nums1:
            if i in counter2 and counter2[i] > 0:
                result.append(i)
                counter2[i] -= 1
        return result



print(intersect(nums2 = [4,9,5], nums1 = [9,4,5,9,8,4]))