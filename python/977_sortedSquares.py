def sortedSquares(nums):
    result = []
    for i in nums:
        result.append(abs(i)**2)
    return sorted(result)

print(sortedSquares(nums = [-7,-3,2,3,11])) # [0, 1, 9, 16, 100]