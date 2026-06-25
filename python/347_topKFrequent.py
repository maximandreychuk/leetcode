def topKFrequent(nums, k):
    counter = {}
    for i in nums:
        counter[i] = counter.get(i, 0) + 1
    sorted_counter = sorted(counter.items(), key=lambda item: -item[1])
    result = []
    count = 0
    while count < k:
        result.append(sorted_counter[count][0])
        count += 1
    return result
print(topKFrequent(nums = [1, 1, 1, 2, 2, 3], k = 2))

# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
