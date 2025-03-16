def minElement(nums):
    import math
    m = math.inf
    for n in nums:
        n = sum([int(i) for i in str(n)])
        if n < m:
            m = n
    return m

minElement(nums = [10,12,13,14])
#done, not optimize